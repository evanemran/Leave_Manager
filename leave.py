import pandas as pd
from datetime import datetime, timedelta

class LeaveManager:
    def __init__(self, excel_file_path='leave_records.xlsx'):
        self.excel_file_path = excel_file_path
        self.leaves_df = pd.DataFrame(columns=['Leave Date', 'Total Days', 'Leave Type', 'Remarks'])

    def apply_leave(self, leave_date, total_days, leave_type, remarks):
        leave_info = {
            'Leave Date': leave_date,
            'Total Days': total_days,
            'Leave Type': leave_type,
            'Remarks': remarks
        }
        self.leaves_df = self.leaves_df._append(leave_info, ignore_index=True)
        self._update_excel()

    def _update_excel(self):
        self.leaves_df.to_excel(self.excel_file_path, index=False)

    def show_leave_status(self):
        print("Current Leave Status:")
        print("+------------+------------+------------+---------------------+")
        print("| Leave Date | Total Days | Leave Type | Remarks             |")
        print("+------------+------------+------------+---------------------+")

        for index, row in self.leaves_df.iterrows():
            leave_date = row['Leave Date']
            total_days = row['Total Days']
            leave_type = row['Leave Type']
            remarks = row['Remarks']

            print(f"| {leave_date} | {total_days:^9}  | {leave_type:^10} | {remarks:<24} |")

        print("+------------+------------+--------------+-------------------+")

    def calculate_remaining_leaves(self):
        # Add your leave policy logic here
        # For example, subtract used leaves from total allowed leaves
        total_allowed_leaves = 20
        used_leaves = self.leaves_df['Total Days'].sum()
        remaining_leaves = total_allowed_leaves - used_leaves
        print(f"Remaining Leaves: {remaining_leaves} days")

# Example Usage:
leave_manager = LeaveManager()

# Apply leave
leave_manager.apply_leave('2024-02-20', 2, 'Casual', 'Family trip')

# Show leave status
leave_manager.show_leave_status()

# Calculate remaining leaves
leave_manager.calculate_remaining_leaves()
