# Open file
open(FH, "data/advent3.in") or die "Died... Can't open file";

# Zet allemaal op één lijn
my $input = join(" ", <FH>);

# Match
my @matches = $input =~ /mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)/g;
my $result = 0;
my $enable = 1;

foreach (@matches) {
    if ($_ =~ /do\(\)/) {
        $enable = 1;
    }
    elsif ($_ =~ /don't\(\)/) {
        $enable = 0;
    }
    elsif ($enable) {
        my @operands = $_ =~ /[0-9]+/g;
        $result += @operands[0] * @operands[1];
    }
}

print $result;

close;
