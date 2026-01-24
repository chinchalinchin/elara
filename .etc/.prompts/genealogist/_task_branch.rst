.. TASK: BRANCH BREAKOUT
..
..          - Break out the {{ new_branch }} into a new diagram.
..          - Starting Node: {{ starting_node }}
..          - Select a starting shade. The process for selecting a shade for a new branch is as follows: Find the other branches that exit from the same source branch, and using distance in the color space as a measure of time, find the next shade of the color group in the gradient. In other words, if a branch already has a green exit, then the next exit should be a lighter shade of green. If there are no exit points in the branch yet, then the color should be selected by adjacency in the (R,G,B) space so that the branch color flows naturally from the current shade in the gradient.
..          - Leave an exit node in the {{ source_branch}} diagram the same shade as the starting shade of the new branch.