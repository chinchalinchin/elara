.. NOTE: This document is formatted with RestructuredText (RST)
..
.. # FAMILY TREE DEVELOPMENT
..
..      - COMMENTS: All comments in this documents are denoted with "..". Comments are meant to provide context. They should be regarded as iron-clad instructions. If it has not been explicitly stated in a comment, then assume it does not apply.
..      - GOAL: Using mermaid, develop and complete the exhaustive family tree of the {{ family }}, given below, from the first ancestor, {{ first_ancestor }} up to the present day.
..      - TASK: The TASK section contains the current directives.
..
.. ## COLOR & STYLE
..
..      **GUIDELINES**
..
..      - Use the principles of Material UI when making updates to the styles.
..      - Use the principles of Color Theory and Color Wheels when selecting new colors.
..      - Make sure the mermaid graphs are well-commented, but on the flip side, don't be too verbose.
..
..      **GRADIENT**
..
..      - Color gradient is used to visualize the descent from the earlier generations (Darker) to the later generations (Lighter).
..      - Color gradient applies to all shades except Special and External, which have a only single shade.
..
..      **PALETTE**
..
..      - Branch 1 Starting Shade (Hex Code): #311B92
..      - Branch 2, Starting Shade (Hex Code): #283593
..      - Branch 3, Starting Shade (Hex Code): #7E57C2
..      - Branch 4, Starting Shade (Hex Code): #880E4F
..      - Branch 5, Starting Shade (Hex Code): #01579B
..      - Branch 6, Starting Shade (Hex Code): #1565C0
..      - Branch 7, Starting Shade (Hex Code): #00695C
..      - Branch 8 , Starting Shade (Hex Code): #0288D1
..      - Branch 9, Starting Shade (Hex Code): #BF360C
..      - Special: Represents Special Individuals, Shade (Hex Code): #00897B
..      - External: Connections of female descendants of male lines to their spouses, Shade (Hex Code): #FFFFFF
..
.. ## NODES
..
..      **Shapes**
..
..      !!! note
..          `<>` are open labels. Assign them before prompting.
..
..      - <> (): 
..      - <> {{}}: Hexagons.
..      - <> ([]): Stadium-shaped Node
..      - Generic Male of Male Descent []: Rectangles
..      - Generic Female of Male Descent {}: Diamonds
..      - Generic Male of Female Descent [/\]: Inverse Trapezoid
..      - Generic Female of Female Descent [\/]: Trapezoid
..      - External Node: Plain Rectangle
..      - Framed Rectangle [[]]: Exit Points of Branches.
..      - Framed Circles ((())): Entry through Branches
..
..      **Labels**
..  
..      - (*Required*) Name
..      - (*Required*) Birth & Death Years
..  
..      Other acceptable labels:
..
..      - Renowned Scientist
..      - Jesuit Affiliation
..      - High Masonic Rank
..      - High Military Rank
..      - Secret Society Affiliations
..      - High Political Office
..      - Known Aliases
.. 
..      Add labels freely, but be conservative. Don't dilute of a label with an overabundance frivolous labels.
..
.. ## RELATIONS
.. 
..      **Marriage**
..
..      - The relations between husbands and wives should include the year they were married (if they were married), prefixed with "m. <year>". 
..      - Dotted lines indicate the marriage of cousins.
..      - Thick lines indicates the marriage of a daughter to an external family. Only the last name of the external connection should be listed.
..      
..      **End of Lineage**
..
..      - The relation between an ancestor and their descendant who had no issue should be included. Lines that end with a "X" denote this relationship.
..      - The "X" should terminate on the final descendant of this branch. Do not add an extra node for the exit.
..      - Once a branch reaches this point, it does not need to factor into further searches.
..      - Once a branch is terminated, this should retroactively turn the prior connections from (-->) into dots (--o), so the lines that end can be tracked down the diagram. The rule should apply up to the node where the ancestor rejoins the (-->) flow.
..      
..      Do not terminate a line (--x) unless you have conclusive proof if it is terminated. **YOU MUST PROVIDE THE EVIDENCE BEFORE TERMINATING A NODE**. Any terminations that are not accompanied by documentation will be rejected, so do not waste your time.
..
.. ## GUIDELINES
..
..      1. Do not try to complete the graph in a single turn. This is meant to be an iterative (Agile) process. It is fine to leave open nodes if you don't have enough information to complete that node.
..      2. This project has been meticulously assembled. Please respect that by only contributing quality entries.
..      3. This project requires empirical verification. Do not infer details.
..      4. Be on the look out for any discrepancies. Advise, but do not change, if you discover any information that contradicts the existing diagram.
..      5. If a date is unknown, approximate it and use a "?" to denote uncertainty.
..      6. Generations should always be aligned to descending rows.
..      7. Do not remove nodes from the tree.
..      8. DO NOT REMOVE NODES FROM THE TREE!
..      9. **DO**. **NOT**. **REMOVE**. **NODES**. **FROM. **THE*. **TREE*.
..
.. ## TASK
..
..      {{ task}}
..
.. ## OUTPUT
.. 
..      - Your output does not need to be RST. Output the mermaid diagram in whatever native format is easiest, and include a list of changes that were applied.
..      - Only include the graph you are updating, but include *THE FULL GRAPH*. **DO NOT DELETE ANY NODES**.
