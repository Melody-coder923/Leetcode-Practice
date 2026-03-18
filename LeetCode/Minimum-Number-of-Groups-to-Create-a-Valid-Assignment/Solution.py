// 1) we can have only x or x - 1 as group size ie in one group how many
//    elements we are keeping
// eg for 7 we can have (2,1) -> 1 1 1 1 1 1 1 
//                      (3,2) -> 3 2 2
//                      (4,3) -> 4 3
//                      (5,4) -> not possible since no of groups we get is 7/4 = 1
//                               and in a group we can have 5 or 4 elements max but 
//                               we are left with 7%4 = 3 > groups we can have here
//                      (6,5) -> not possible
//                      (7,6) -> groups = 7/6 = 1 rem = 7%6 = 1 so yes possible
//                      (8,7) -> groups = 7/7 = 1 rem = 0 so possible