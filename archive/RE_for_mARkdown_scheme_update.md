# TOPO Tags

RE URI: `/w+_\d{3}[EW]\d{3}[NS]_\w` < wrong, does not catch regionURIs (Sham_RE)
Shorter: `\w+_\w{1,2}`

## BLACK (old: 00): - requires review

@T\d1@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+
@T\d2@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+
@T\d3@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+
@T\d4@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

### Final RE (paste to the Scheme) - ADDED

TOPONYMS I (REQUIRE REVIEW)|@T\d1@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+|@T\d2@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+|@T\d3@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+|@T\d4@\w+_\w{1,2}(,\w+_\w{1,2})*@-@(book|dir|ethno|minor|person|review|water|wrong)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

## YELLOW (old: ta): - requires additional review

@T\d1@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+
@T\d2@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+
@T\d3@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+
@T\d4@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

### Final RE (paste to the Scheme) - ADDED

TOPONYMS II (REQUIRE ADDITIONAL REVIEW)|@T\d1@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+|@T\d2@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+|@T\d3@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+|@T\d4@\w+_\w{1,2}(,\w+_\w{1,2})+@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

## ORANGE (old: ff): - final

@T\d1@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+
@T\d2@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+
@T\d3@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+
@T\d4@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

### Final RE (paste to the Scheme)

TOPONYMS III (FINAL)|@T\d1@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+|@T\d2@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+|@T\d3@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+|@T\d4@\w+_\w{1,2}@-@(true)@[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+[ ~\n]+\w+

# ROOT Tags

## RED (old: fr)

see below

### Final RE (paste to the Scheme) - added

OPEN TAGGING PATTERN (UNKNOWN)|@[A-Z]{3}@[A-Z]{3,}@[A-Za-z]+@-@(0+|review)@

## GREEN (old: tr)

see below

### Final RE (paste to the Scheme) - added

OPEN TAGGING PATTERN (TRUE)|@[A-Z]{3}@[A-Z]{3,}@[A-Za-z]+@-@true@

## BLUE (old: tr / categorized)

see below

### Final RE (paste to the Scheme) 

OPEN TAGGING PATTERN (TRUE, CATEGORIZED)|@[A-Z]{3}@[A-Z]{3,}@[A-Za-z_]+@-@true@
