

def read_data(filename):
    """
    Reads data from filename, where each row is a training example of a 28x28
    grayscale image.
    """
    data = []
    f = open(filename, 'r')
    for line in f:
        row = []
        vals = line.split()
        for v in vals:
            row.append(int(float(v)))
        data.append(row)
    f.close()
    return data

def add_output(data, y):
    """
    Adds the output value y to data.
    """
    aug_data = []
    for line in data:
        aug_data.append(line + [y])
    return aug_data

def write_data(filename, data):
    """
    Write data to a file called filename.
    """
    f = open(filename,'w')
    for row in data:
        for i,val in enumerate(row):
            if i < len(row)-1: 
                f.write(str(val) + " ")
            else:
                f.write(str(val) + "\n")
    f.close()

def write_check_data(filename,data):
    """
    Write data in matrix form to visually check that everything's fine.
    """
    f = open(filename, 'w')
    for i,row in enumerate(data):
        if i % 100 == 0:
            for j,n in enumerate(row):
                f.write("{:4d}".format(n))
                if (j+1)%28 == 0:
                    f.write('\n')
            f.write("\n\n")
    f.close()

def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    data = []
    for n in nums:
        filename = "data_products/data" + str(n) + ".txt"
        data = data + add_output(read_data(filename), n)
    
    a = int(len(data)*0.6)
    b = int(len(data)*0.8)
    # Write training data
    write_data('digits_training.txt', data[:a])
    # Write cross validation data
    write_data('digits_CV.txt', data[a:b])
    # Write test data
    write_data('digits_test.txt', data[b:])
    # Write visual check file
    write_check_data('check.txt', data)

if __name__ == "__main__":
    main()
