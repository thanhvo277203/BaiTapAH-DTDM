from ._anvil_designer import Form2Template
from anvil import *


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set up the options for sorting algorithms
    self.sort_algorithms = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Merge Sort"]
    self.drop_down_sort_algorithm.items = self.sort_algorithms

  def button_sort_click(self, **event_args):
      # Get the input list of numbers from the TextBox
      input_list = [int(x.strip()) for x in self.text_box_input.text.split(",")]
        
      # Get the selected sorting algorithm
      selected_algorithm = self.drop_down_sort_algorithm.selected_value
        
      # Sort the input list using the selected algorithm
      sorted_list = self.sort(input_list, selected_algorithm)
        
      # Display the sorted list in the output TextBox
      self.text_box_output.text = ", ".join(map(str, sorted_list))

  def sort(self, input_list, algorithm):
        # Sorting algorithms implementations
        if algorithm == "Insertion Sort":
            return self.insertion_sort(input_list)
        elif algorithm == "Selection Sort":
            return self.selection_sort(input_list)
        elif algorithm == "Bubble Sort":
            return self.bubble_sort(input_list)
        elif algorithm == "Merge Sort":
            return self.merge_sort(input_list)

  def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

  def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

  def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

  def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr

# Run the app
if __name__ == '__main__':
    app = Form2()
    app.run()
    
