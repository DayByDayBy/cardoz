import graphviz

# entity-relationship diagram
er = graphviz.Digraph('ERD', format='png')
er.attr(rankdir='LR', size='8,5')

# users table
er.node('Users', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>users</B></TD></TR>
<TR><TD>id</TD><TD>PK</TD></TR>
<TR><TD>username</TD><TD></TD></TR>
<TR><TD>email</TD><TD></TD></TR>
</TABLE>>''')

# cards table
er.node('Cards', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>cards</B></TD></TR>
<TR><TD>nameShort</TD><TD>PK</TD></TR>
<TR><TD>name</TD><TD></TD></TR>
<TR><TD>type</TD><TD></TD></TR>
<TR><TD>suit</TD><TD></TD></TR>
<TR><TD>value</TD><TD></TD></TR>
<TR><TD>meaningUp</TD><TD></TD></TR>
<TR><TD>meaningRev</TD><TD></TD></TR>
<TR><TD>description</TD><TD></TD></TR>
</TABLE>>''')

# spreads table
er.node('Spreads', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>spreads</B></TD></TR>
<TR><TD>id</TD><TD>PK</TD></TR>
<TR><TD>name</TD><TD></TD></TR>
<TR><TD>description</TD><TD></TD></TR>
</TABLE>>''')

# spread Positions table
er.node('SpreadPositions', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>spread_positions</B></TD></TR>
<TR><TD>id</TD><TD>PK</TD></TR>
<TR><TD>spread_id</TD><TD>FK → spreads.id</TD></TR>
<TR><TD>position</TD><TD></TD></TR>
<TR><TD>label</TD><TD></TD></TR>
</TABLE>>''')

# readings table
er.node('Readings', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>readings</B></TD></TR>
<TR><TD>id</TD><TD>PK</TD></TR>
<TR><TD>user_id</TD><TD>FK → users.id</TD></TR>
<TR><TD>spread_id</TD><TD>FK → spreads.id</TD></TR>
<TR><TD>question</TD><TD></TD></TR>
<TR><TD>timestamp</TD><TD></TD></TR>
<TR><TD>reading_text</TD><TD></TD></TR>
<TR><TD>notes</TD><TD></TD></TR>
</TABLE>>''')

# reading Cards table
er.node('ReadingCards', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>reading_cards</B></TD></TR>
<TR><TD>id</TD><TD>PK</TD></TR>
<TR><TD>reading_id</TD><TD>FK → readings.id</TD></TR>
<TR><TD>card_id</TD><TD>FK → cards.nameShort</TD></TR>
<TR><TD>position_index</TD><TD></TD></TR>
<TR><TD>reversed</TD><TD></TD></TR>
</TABLE>>''')

# relationships
er.edge('Users', 'Readings', label='1 → ∞')
er.edge('Spreads', 'Readings', label='1 → ∞')
er.edge('Spreads', 'SpreadPositions', label='1 → ∞')
er.edge('Readings', 'ReadingCards', label='1 → ∞')
er.edge('Cards', 'ReadingCards', label='1 → ∞')

er.render('/mnt/data/tarot_erd', view=False)
'/mnt/data/tarot_erd.png'