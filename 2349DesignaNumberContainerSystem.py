# Design a number container system that can do the following:

# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:

# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
class NumberContainers:

    def __init__(self):
        self.indexes_vs_number= defaultdict()
        self.number_vs_indexes=dict()

    def change(self, index: int, number: int) -> None:
        if index not in self.indexes_vs_number:
            self.indexes_vs_number[index]=number
            if number in self.number_vs_indexes:
                self.number_vs_indexes[number].append(index)
            else:
                self.number_vs_indexes[number]=[index]

        else:
            previous_value=self.indexes_vs_number[index]
            if previous_value!=number:

                indexes=self.number_vs_indexes[previous_value]

                indexes.remove(index)
                if len(indexes)==0:
                    del self.number_vs_indexes[previous_value]
                self.indexes_vs_number[index]=number
                if number in self.number_vs_indexes:
                    self.number_vs_indexes[number].append(index)
                else:
                    self.number_vs_indexes[number]=[index]

    def find(self, number: int) -> int:
        if number in self.number_vs_indexes:
            return min(self.number_vs_indexes[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)