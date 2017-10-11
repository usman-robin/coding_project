#/usr/bin/perl

@a = qw(
  hello
  world
  hello
  goodbye
  earthlings
);
@b = qw(
  earthlings
  say
  hello
  earthlings
);

my @int;
OUTER: for my $x (@a) {
  for my $y (@b) {
    if ($x eq $y) {
      push @int, $x;
      next OUTER;
    }
  }
}
for my $x (@int) {
    print("$x\n")
}