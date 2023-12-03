def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            result.append(i)
            for j in range(2, num_columns + 1):
                if j != num_columns:
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))


print_operation_table(lambda x, y: x * y)
