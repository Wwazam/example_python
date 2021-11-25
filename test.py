def index(i, j):
    n = 5
    return i*n + j

def out_of_range(index):
    return not (index in [0,4])

def choisir_case():
    i = int(input())
    j = int(input())
    if out_of_range(i) or out_of_range(j):
        return "NON"
    return index(i,j)

def get_neighbours_index(i, j):
    ma_list = []
    for y_offset in range(-1,2):
        for x_offset in range (-1,2):
            if y_offset == 0 and x_offset == 0:
                continue

            a=i+y_offset
            b=j+x_offset

            if(out_of_range(a) or out_of_range(b)):
                continue
            ma_list.append(index(a, b))
    return ma_list


if __name__ == "__main__":
    print(get_neighbours_index(3, 3))

# GO LOOK AT THAT https://learngitbranching.js.org/
