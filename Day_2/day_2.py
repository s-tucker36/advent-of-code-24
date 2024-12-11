class RedNoseReports:
    def __init__(self, input_file):
        self.input_file = input_file
        self.reports = []

    def get_reports(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.reports.append([int(num) for num in line.strip().split(' ')])

    def check_safety(self):
        safety_count = 0
        for report in self.reports:
            if self.determine_safety(report):
                safety_count += 1
        print("safety count without problem dampener: ", safety_count)

        safety_count = 0
        for report in self.reports:
            for i in range(len(report)):
                temp = report.pop(i)
                if self.determine_safety(report):
                    safety_count += 1
                    break
                report.insert(i, temp)
        print("safety count with problem dampener: ", safety_count)

    def determine_safety(self, report):
        ascending = None
        
        for i in range(1, len(report)):
            if ascending is None:
                ascending = report[i] > report[i - 1]
            
            if ascending and report[i] < report[i - 1]:
                return False
            elif not ascending and report[i] > report[i - 1]:
                return False
            
            if not (abs(report[i] - report[i - 1]) >= 1 and abs(report[i] - report[i - 1]) <= 3):
                return False
        return True

if __name__ == "__main__":
    red_nose_reports = RedNoseReports('input.txt')
    red_nose_reports.get_reports()
    red_nose_reports.check_safety()
