package DB_perl;
use strict;
use DBI;
use autodie;
use Sys::Syslog qw(:standard :macros);

#########################
## 执行SQL语句，返回结果集
## 输入：SQL命令
## 输出：结果集（数组+Hash）
#########################
sub sql_exec {
    my ( $cmd, $ip )= @_ ;
    if ( !defined($cmd) || $cmd eq "" ) {
	print "Err:SQL_command is NULL !\n";
	return -1;
    }

    my $dbh = !defined($ip) ? &waa_connect() : &waa_connect($ip);
    if ( $dbh == -1 ) {
	print "Err:SQL_connect is fail!\n";
	return -1;
    }

    my @temp;
    eval {
	$cmd =~s/^\s+//g;
	my $oper = substr( $cmd, 0, 6 );

	if ( $oper =~ /select/i ) {
	    my $sqr = $dbh->prepare( $cmd );
	    $sqr->execute();
	    while ( my $hash_ref = $sqr->fetchrow_hashref() ) {
		push( @temp, $hash_ref );
	    }
	    $sqr->finish;
	}
	else {
	    $dbh->do( $cmd );
	}
    };
    if ( $@ ) {
	syslog('warning', 'SQL_Command_Fail ! : $@ \n SQL_CMD : $cmd\n');
	$dbh->disconnect;
	return -1;
    }

    $dbh->disconnect;
    return @temp;
}

#########################
## 数据库连接操作
## 输入：1-IP地址、2-数据库名、3-用户名、4-密码
## 输出：连接句柄，错误返回-1
#########################
sub waa_connect {
    my $addr   = shift || "localhost";
    my $DBname = shift || "waa";
    my $user   = shift || "forceview";
    my $passw  = shift || "forceview";
    my $dbc;
    eval {
	$dbc = DBI->connect( "DBI:mysql:database=$DBname;host=$addr",
	    "$user", "$passw", { RaiseError => 1 } )
	  || die "Can’t connect: $DBI::errstr\n";
	$dbc->do("SET character_set_client='utf8'");
	$dbc->do("SET character_set_connection='utf8'");
	$dbc->do("SET character_set_results='utf8'");
    };
    if ( $@ ) {
	syslog('warning', 'Err:Connect DB Fail !:$@\n');
	$dbc->disconnect;
	return -1;
    }

    return $dbc;
}

1;
