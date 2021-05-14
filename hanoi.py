import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    disk_peg = []
    props = []
    for disk in disks:
        for peg in pegs:
            props.append(disk + peg)
            disk_peg.append(disk + peg)
            props.append("N" + disk + peg)
    domain_text = "Propositions:\n"
    for prop in props:
        domain_text += (prop + " ")

    domain_text += "\nActions:\n"
    for d in disks:
        for p in pegs:
            for p2 in pegs:
                if p != p2:
                    action_name = "M" + d + p + p2
                    domain_text += ("Name: " + action_name + "\n")
                    domain_text += "pre: "
                    domain_text += (d + p + " ")
                    for i in range(int(d[2])):
                        domain_text += ("N" + "d_" + str(i) + p2 + " ")  # d will be the smallest in the new peg
                    for i in range(int(d[2])):
                        domain_text += ("N" + "d_" + str(i) + p + " ")  # d is be the smallest in the prev peg
                    domain_text += "\n"
                    domain_text += "add: "
                    domain_text += (d + p2 + " ")
                    domain_text += ("N" + d + p + " ")
                    domain_text += "\n"
                    domain_text += "delete: "
                    domain_text += (d + p + " ")
                    domain_text += ("N" + d + p2 + " ")
                    domain_text += "\n"
    domain_file.write(domain_text)
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    problem_text = "Initial state: "
    for d in disks:
        problem_text += (d + pegs[0] + " ")
        for p in pegs[1:]:
            problem_text += ("N" + d + p + " ")
    problem_text += "\nGoal state: "
    for d in disks:
        problem_text += (d + pegs[-1] + " ")
        for p in pegs[:-1]:
            problem_text += ("N" + d + p + " ")
    problem_file.write(problem_text)
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs


    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
