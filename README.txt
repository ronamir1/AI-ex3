208345561
208271767
*****
Comments:
For the hanoi domain and problem files we decided to encode the propositions as d_ip_j representing
that disk number i is in peg number j and Nd_ip_j to represent that disk number i is not in peg number
j. The only possible action is moving disks from one peg to another - so the actions are of type
Md_ip_jp_k meaning move disk i from peg j to peg k. To make sure actions are legal the preconditions
require that to move a disk from peg j to peg k, that disk will be the smallest in the new peg
which is required for it to be moved there as it cannot be placed on a smaller disk, and that the
disk is the smallest in the previous peg because that means it is on top - if there is a smaller
disk in the previous peg it must be on top of the disk we are trying to move and hence we can't move it.

The initial state in the problem has all disks on peg number 0 indicated by d_ip_o and also
says that no disk is on any other peg indicated by Nd_ip_j for j>0 to j = m-1.
The goal state has all the disks on peg number m-1 indicated by d_ip_m-1 and also says that no
disk is on any other peg indicated by N_d_ip_j for j=0 to j = m-2.

Because of the way we constructed the domain there is no way for a smaller disk to be under a bigger
disk so as we start with all disks in order on the first (index 0) peg we get to the goal state
with all disks in order on the last peg (index m-1).
