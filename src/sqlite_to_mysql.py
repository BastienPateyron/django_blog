#! /usr/bin/env python

import sys, re

def main():
    print ("SET sql_mode='NO_BACKSLASH_ESCAPES';")
    lines = sys.stdin.read().splitlines()
    for line in lines:
        processLine(line)

def processLine(line):
    if (
        line.startswith("PRAGMA") or 
        line.startswith("BEGIN TRANSACTION;") or
        line.startswith("COMMIT;") or
        line.startswith("DELETE FROM sqlite_sequence;") or
        line.startswith("INSERT INTO \"sqlite_sequence\"") or
        line.startswith("INSERT INTO sqlite_sequence")
       ):
        return
    line = line.replace("AUTOINCREMENT", "AUTO_INCREMENT")
    line = line.replace("DEFAULT 't'", "DEFAULT '1'")
    line = line.replace("DEFAULT 'f'", "DEFAULT '0'")
    line = line.replace(",'t'", ",'1'")
    line = line.replace(",'f'", ",'0'")
    line = line.replace("COLLATE NOCASE_UTF8", "")
    line = line.replace("DEFERRABLE INITIALLY DEFERRED", "")
    line = line.replace("integer DEFAULT 0 NOT NULL", "integer NOT NULL DEFAULT 0")
    line = line.replace("integer DEFAULT 1 NOT NULL", "integer NOT NULL DEFAULT 1")
    line = line.replace("varchar ", "varchar(255) ")
    line = line.replace("varchar,", "varchar(255),")
    line = line.replace("varchar)", "varchar(255))")
    line = line.replace(" BLOB ", " LONGBLOB ")
    line = re.sub('CHECK \((.*?)\)', '', line)
    line = re.sub('CREATE INDEX.*?;', '', line)
    line = re.sub('CREATE UNIQUE INDEX.*?;', '', line)

    in_string = False
    newLine = ''
    for c in line:
        if not in_string:
            if c == "'":
                in_string = True
            elif c == '"':
                newLine = newLine + '`'
                continue
        elif c == "'":
            in_string = False
        newLine = newLine + c
    print (newLine)

if __name__ == "__main__":
    main()


