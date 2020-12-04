import sys
import re


def parse_file(filename):
    passports = []
    passport = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                passports.append(passport)
                passport = {}
            else:
                entries = line.split(' ')
                for entry in entries:
                    fields = entry.split(':')
                    passport[fields[0]] = fields[1]
    if passport:
        passports.append(passport)
    return passports


def check_field(field, value):
    if field == 'byr':
        m = re.fullmatch(r'(\d{4})', value)
        if m:
            v = int(m.group(1))
            if 1920 <= v <= 2002:
                return 1
    elif field == 'iyr':
        m = re.fullmatch(r'(\d{4})', value)
        if m:
            v = int(m.group(1))
            if 2010 <= v <= 2020:
                return 1
    elif field == 'eyr':
        m = re.fullmatch(r'(\d{4})', value)
        if m:
            v = int(m.group(1))
            if 2020 <= v <= 2030:
                return 1
    elif field == 'hgt':
        m = re.fullmatch(r'(\d+)(cm|in)', value)
        if m:
            v = int(m.group(1))
            if m.group(2) == 'cm':
                if 150 <= v <= 193:
                    return 1
            else:
                if 59 <= v <= 76:
                    return 1
        else:
            print("no match hgt")
    elif field == 'hcl':
        m = re.fullmatch(r'#[0-9a-f]{6}', value)
        if m:
            return 1
    elif field == 'ecl':
        m = re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', value)
        if m:
            return 1
    elif field == 'pid':
        m = re.fullmatch(r'[0-9]{9}', value)
        if m:
            return 1


def part_a(filename):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = parse_file(filename)
    valid_count = 0
    for passport in passports:
        valid = 1
        for field in required:
            if field not in passport:
                valid = 0
        if valid:
            valid_count += 1
    return valid_count


def part_b(filename):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = parse_file(filename)
    valid_count = 0
    for passport in passports:
        valid = 1
        for field in required:
            if field not in passport:
                valid = 0
            else:
                if not check_field(field, passport[field]):
                    print("fails on {}:{}".format(field, passport[field]))
                    valid = 0
        if valid:
            valid_count += 1
    return valid_count
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day04.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day04.txt'))


if __name__ == "__main__":
    entry()
