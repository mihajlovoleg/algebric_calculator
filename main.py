class MatrixOperations:

    def __init__(self, matrix_count, matrices):
        self.matrix_count = matrix_count
        self.matrices = matrices
        

    def print_matrix(self, matrix):
        for i in range(len(matrix)):
            print()
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=' ')

    def matrix_multiply(self):
        matrix_a, matrix_b = self.matrices[0], self.matrices[1]
        matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    
        print("\nMatrix A:")
        self.print_matrix(matrix_a)
        print()

        print("\nMatrix B:")
        self.print_matrix(matrix_b)

        print()

        print("\nResult Matrix C:")
        self.print_matrix(matrix_c)

        print()

    def create_matrix(self, matrix_count, operation):
            
        if self.matrix_count == 1:    
            matrix_size = input('Enter the matrix size (example: 3x2): ')

            if 'x' not in matrix_size:
                print('Wrong separator! Try again!')
                return self.create_matrix()
            else:
                matrix_size_substring = matrix_size.split('x')

                matrix = [[0] * int(matrix_size_substring[1]) for _ in range(int(matrix_size_substring[0]))]

                for row in range(int(matrix_size_substring[0])):
                    for col in range(int(matrix_size_substring[1])):
                        matrix_value = int(input(f'Enter the value in {row+1} row and {col+1} column for matrix: '))
                        matrix[row][col] = matrix_value

                        # print("\nMatrix:")
                        # for i in range(len(matrix)):
                        #     print()
                        #     for j in range(len(matrix[0])):
                        #         print(matrix[i][j], end=' ')
                        self.print_matrix(matrix)

                return matrix
            
        elif self.matrix_count == 2:
            first_matrix_size = input('Enter the size of first matrix (example 3x2): ')
            second_matrix_size = input('Enter the size of second matrix size (example 3x2): ')

            if 'x' not in first_matrix_size or 'x' not in second_matrix_size:
                print('Wrong separator! Try again!')
                return self.create_matrix()
            else:

                first_matrix_size_substring = first_matrix_size.split('x')
                second_matrix_size_substring = second_matrix_size.split('x')

                print(first_matrix_size_substring, second_matrix_size_substring)
                matrix_a = []
                matrix_b = []
                
                if operation == 2:
                    if first_matrix_size_substring[1] != second_matrix_size_substring[0]:
                        print('You entered wrong matrix`s format (MxP = PxS). Try again!')
                        return self.create_matrix(2)
                    else:
                        matrix_a = [[0] * int(first_matrix_size_substring[1]) for i in range(int(first_matrix_size_substring[0]))]
                        matrix_b = [[0] * int(second_matrix_size_substring[1]) for i in range(int(second_matrix_size_substring[0]))]

                        for row in range(int(first_matrix_size_substring[0])): 
                            for col in range(int(first_matrix_size_substring[1])):

                                matrix_value = int(input(f'Enter the value in {row+1} row and {col+1} column for matrix A: '))
                                matrix_a[row][col] = matrix_value 

                                # for i in range(len(matrix_a)):
                                #     print()
                                #     for j in range(len(matrix_a[0])):
                                #         print(matrix_a[i][j], end = ' ')
                                self.print_matrix(matrix_a)

                                print()
                                

                                



                        for row in range(int(second_matrix_size_substring[0])): 
                            for col in range(int(second_matrix_size_substring[1])): 

                                matrix_value = int(input(f'Enter the value in {row+1} row and {col+1} column for matrix B: '))
                                matrix_b[row][col] = matrix_value 

                                # for i in range(len(matrix_b)):
                                #     print()
                                #     for j in range(len(matrix_b[0])):
                                #         print(matrix_b[i][j], end = ' ')
                                self.print_matrix(matrix_b)
                                    
                                print()
                else:
                    matrix_a = [[0] * int(first_matrix_size_substring[1]) for i in range(int(first_matrix_size_substring[0]))]
                    matrix_b = [[0] * int(second_matrix_size_substring[1]) for i in range(int(second_matrix_size_substring[0]))]

                    for row in range(int(first_matrix_size_substring[0])): 
                        for col in range(int(first_matrix_size_substring[1])): 

                            matrix_value = int(input(f'Enter the value in {row+1} row and {col+1} column for matrix A: '))
                            matrix_a[row][col] = matrix_value 

                            # for i in range(len(matrix_a)):
                            #     print()
                            #     for j in range(len(matrix_a[0])):
                            #         print(matrix_a[i][j], end = ' ')
                            self.print_matrix(matrix_a)

                            print()
                                

                                



                    for row in range(int(second_matrix_size_substring[0])): 
                        for col in range(int(second_matrix_size_substring[1])): 

                            matrix_value = int(input(f'Enter the value in {row+1} row and {col+1} column for matrix B: '))
                            matrix_b[row][col] = matrix_value 

                            # for i in range(len(matrix_b)):
                            #     print()
                            #     for j in range(len(matrix_b[0])):
                            #         print(matrix_b[i][j], end = ' ')
                                    
                            #     print()
                            self.print_matrix(matrix_b)

                return matrix_a, matrix_b

         





    def find_rank(self, matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if matrix else 0

        rank = 0
        pivot_column = 0

        for pivot_row in range(num_rows):
            if pivot_column >= num_cols:
                break

            
            non_zero_row = pivot_row
            while non_zero_row < num_rows and matrix[non_zero_row][pivot_column] == 0:
                non_zero_row += 1

            
            if non_zero_row < num_rows:
                
                rank += 1

                
                matrix[pivot_row], matrix[non_zero_row] = matrix[non_zero_row], matrix[pivot_row]

                
                pivot_element = matrix[pivot_row][pivot_column]
                matrix[pivot_row] = [elem / pivot_element for elem in matrix[pivot_row]]

                
                for other_row in range(num_rows):
                    if other_row != pivot_row:
                        factor = matrix[other_row][pivot_column]
                        matrix[other_row] = [elem - factor * matrix[pivot_row][i] for i, elem in enumerate(matrix[other_row])]

                # Переход до наступного стовбця
                pivot_column += 1

        return rank

    def find_determinant(self, matrix):

        def det_recursive(matrix):
            if len(matrix) != len(matrix[0]):
                print('Matrix must be square!')
                return self.find_determinant()


            elif len(matrix) == 2 and len(matrix[0]) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            
            det_value = 0

            for j in range(len(matrix)):
                det_value += (-1) ** j * matrix[0][j] * det_recursive([row[:j] + row[j+1:] for row in matrix[1:]])

            return det_value
        
        return det_recursive(matrix)
    

    def matrix_sum(self):
        matrix_a, matrix_b = self.matrices[0], self.matrices[1]
        matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            print('Matrices must have the same dimensions for adding. Try again')
            return self.matrix_sum()
        
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                matrix_c[i][j] += matrix_a[i][j] + matrix_b[i][j]

        print("\nMatrix A:")
        self.print_matrix(matrix_a)
        print()

        print("\nMatrix B:")
        self.print_matrix(matrix_b)

        print()

        print("\nResult Matrix C:")
        self.print_matrix(matrix_c)

        print()
        

    def matrix_substract(self):
        matrix_a, matrix_b = self.matrices[0], self.matrices[1]
        matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            print('Matrices must have the same dimensions for substracting. Try again')
            return self.matrix_substract()
        
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                matrix_c[i][j] += matrix_a[i][j] - matrix_b[i][j]

        print("\nMatrix A:")
        self.print_matrix(matrix_a)
        print()

        print("\nMatrix B:")
        self.print_matrix(matrix_b)

        print()

        print("\nResult Matrix C:")
        self.print_matrix(matrix_c)

        print()

        
class VectorOperations:
    def __init__(self):
        self.first_vector_str = ""
        self.second_vector_str = ""
        self.single_vector_str = ""

    def create_vector(self, vector_str):
        return list(map(int, vector_str.split(' ')))

    def vector_multiply(self, first_vector_str, second_vector_str):
        first_vector = self.create_vector(first_vector_str)
        second_vector = self.create_vector(second_vector_str)
        return [first_vector[1] * second_vector[2] - (first_vector[2] * second_vector[1]),
                first_vector[2] * second_vector[0] - (first_vector[0] * second_vector[2]),
                first_vector[0] * second_vector[1] - (first_vector[1] * second_vector[0])]

    def vector_module(self, single_vector_str):
        single_vector = self.create_vector(single_vector_str)
        if len(single_vector) == 2:
            return round((single_vector[0] ** 2 + single_vector[1] ** 2) ** 0.5, 2)
        elif len(single_vector) == 3:
            return round((single_vector[0] ** 2 + single_vector[1] ** 2 + single_vector[2] ** 2) ** 0.5)
        else:
            print('You entered more than 3 numbers, try again!')
            return False

while True:
    print('Welcome to algebraic calculator! Choose what branch you want to use.')
    branch = int(input('Enter the number (1 - matrices, 2 - vectors, 3 - quit): '))
    
    if branch == 1: 
        
        while True:
            print()
            print('1. Matrix multiply\n2. Matrix rank\n 3. Matrix determinant\n 4. Matrix sum\n 5. Matrix subtract\n6. Back to main menu')

            operation = int(input('Choose the operation (enter the number from 1 to 6): '))
            matrix_operations = MatrixOperations(None, None)

            if operation in [1, 2, 3, 4, 5, 6]:
                if operation in [1, 4, 5]:
                    matrix_operations.matrix_count = 2
                    create_matrix_return = matrix_operations.create_matrix(matrix_operations.matrix_count, operation)
                    matrix_operations.matrices = create_matrix_return
                    if operation == 1:
                        matrix_operations.matrix_multiply()
                    elif operation == 4:
                        matrix_operations.matrix_sum()
                    elif operation == 5:
                        matrix_operations.matrix_substract()
                elif operation in [2, 3]:
                    matrix_operations.matrix_count = 1
                    matrix = matrix_operations.create_matrix(matrix_operations.matrix_count, operation)
                    print()
                    if operation == 2:
                        print('Rank of matrix\n')
                        matrix_operations.print_matrix(matrix)
                        print(f'\nis {matrix_operations.find_rank(matrix)}')
                    elif operation == 3:
                        print('Determinant of matrix\n')
                        matrix_operations.print_matrix(matrix)
                        print(f'\nis {matrix_operations.find_determinant(matrix)}')

                elif operation == 6:
                    break

            else:
                print('You choosed the wrong operation, try again.')
                continue
    
    elif branch == 2:
        while True:    
            print()
            print('1. Vector multiply (3D)\n2. Vector module (length) 3D/2D\n3. Back to main menu')
            print()
            operation = int(input('Choose the operation (enter the number from 1 to 3): '))

            vector_operations = VectorOperations()

            if operation in [1, 2, 3]:
                if operation == 1:
                    vector_operations.first_vector_str = input('Enter the numbers separated by space for the first vector: ')
                    vector_operations.second_vector_str = input('Enter the numbers separated by space for the second vector: ')
                    print(*vector_operations.vector_multiply(vector_operations.first_vector_str, vector_operations.second_vector_str))
                    continue

                elif operation == 2:
                    vector_operations.single_vector_str = input('Enter the numbers separated by space for the vector: ')
                    if vector_operations.vector_module(vector_operations.single_vector_str) != False:
                        print(f'Module of vector {vector_operations.create_vector(vector_operations.single_vector_str)} '
                            f'equals {vector_operations.vector_module(vector_operations.single_vector_str)}.')
                        continue
                else:
                    break
            else:
                print('Wrong operation, try again!')
                continue

    elif branch == 3:
        print('Good luck!')
        break

    else:
        print('This branch doesn`t exist! Try again.')
        continue
