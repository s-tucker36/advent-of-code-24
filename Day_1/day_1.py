class DistanceCalculator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.location_ids_left=[]
        self.location_ids_right=[]

    def sort_lists(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                split = line.split()
                self.location_ids_left.append(int(split[0]))
                self.location_ids_right.append(int(split[1]))

        self.location_ids_left.sort()
        self.location_ids_right.sort()

    def get_distance(self):
        total_distance = 0
        for i, j in zip(self.location_ids_left, self.location_ids_right):
            total_distance += abs(i - j)
        print(total_distance)

    def get_similarity_score(self):
        similarity_score = 0
        for i in self.location_ids_left:
            occurences = self.location_ids_right.count(i)
            similarity_score += i *occurences
        print(similarity_score)


if __name__ == "__main__":
    distance_calculator = DistanceCalculator('input.txt')
    distance_calculator.sort_lists()
    distance_calculator.get_distance()
    distance_calculator.get_similarity_score()

