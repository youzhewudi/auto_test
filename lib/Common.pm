package Common;
use strict;
use POSIX 'setsid';

sub become_daemon {
    die "Can't fork" unless defined(my $child = fork);
    exit 0 if $child;
    setsid();
    open(STDIN,  "</dev/null");
    open(STDOUT, ">/dev/null");
    open(STDERR, ">/dev/null");
    chdir '/';
    umask(0);
}

1;
