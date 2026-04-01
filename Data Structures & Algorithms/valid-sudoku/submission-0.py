class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num != '.':

                    row_id = (r, num)
                    col_id = (num, c)
                    box_id = (r//3, c//3, num)

                    if row_id in seen or col_id in seen or box_id in seen:
                        return False

                    seen.add(row_id)
                    seen.add(col_id)
                    seen.add(box_id)
        return True



