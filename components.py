def increment_string(stri):
    strings = ""
    num = ""
    inc = 0

    for i in range(len(stri)):
        if (stri[i].isdigit()):
            num = num + stri[i]
        else:
            strings += stri[i]
    if(num == ""):
       print("No num found in: ", stri)
       return strings
    else:
        inc = int(num) + 1
        fin = strings + str(inc)
        return fin

def make_prime(stri):
    strings = ""
    num = ""

    for i in range(len(stri)):
        if (stri[i].isdigit()):
            num = num+ stri[i]
        else:
            strings += stri[i]
    strings = strings + "'"
    if(num == ""):
        return strings
    fin = strings + num
    return fin

def check_is_prime(label):
    if "'" in label:
        return True
    else: return False

def split_prime_label(label):
    if "'" in label:
        split_label = label.split("'")

        split_label[1] = int(split_label[1])
        print(split_label)
        return split_label

def split_nonprime_label(label):
    if "'" in label:
        pass
    else:
        split_label = []
        split_label.append(label[0])
        split_label.append(label[1:])

        if len(split_label) > 1:
            split_label[1] = int(split_label[1])
        print(split_label)
        return split_label

def split_label_pnp(label):
    split_label = []
    if label == "S":
        pass

    elif "'" in label:
        split_label = label.split("'")
        split_label[1] = int(split_label[1])
    else:
        split_label.append(label[0])
        split_num = label[1:]
        split_label.append(int(split_num))
    return split_label

def transition_to_forward(label):
    new_label = "F" + label[1:]
    return new_label

def transition_to_backward(label):
    if not("B'" in label):
        new_label = "B" + label[1:]
        return new_label


def check_nums_same(labelA, labelB):
    split_labelA = split_label_pnp(labelA)
    split_labelB = split_label_pnp(labelB)
    if split_labelA[1] == split_labelB[1]:
        return True
    else:
        return False

def check_A_greater(labelA, labelB):
    split_labelA = split_label_pnp(labelA)
    split_labelB = split_label_pnp(labelB)
    if split_labelA[1] > split_labelB[1]:
        return True
    else:
        return False

def check_A_less(labelA, labelB):
    split_labelA = split_label_pnp(labelA)
    split_labelB = split_label_pnp(labelB)
    if split_labelA[1] < split_labelB[1]:
        return True
    else:
        return False

# States Tests
def states_test_14(states):
    #Hard Coded for N = 14
    st = []
    st.append("S")
    st.append("B0")
    st.append("B'0")
    st.append("F0")
    # 1s
    st.append("B1")
    st.append("F1")
    st.append("F'1")
    # 2s
    st.append("B2")
    st.append("F2")
    st.append("F'2")
    # 3's
    st.append("B3")
    # Rs
    st.append("R3")
    st.append("R'3")
    st.append("R2")
    st.append("R'2")
    st.append("R'0")

    passes = []
    missing = st.copy()
    failures = []

    for i in range(len(states)):
        if states[i] in st:
            passes.append(states[i])
            missing.remove(states[i])
        elif not(states[i] in st):
            failures.append(states[i])

    print("Number Passed: ", len(passes), "Out of: ", len(st))
    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(st))
    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(st))
    for p in missing:
        print("Missing: ", p)

def states_test_27(states):
    #Hard Coded for N = 27
    st = []
    st.append("S")
    st.append("B0")
    st.append("B'0")
    st.append("F0")
    # 1s
    st.append("B1")
    st.append("F1")
    st.append("F'1")
    # 2s
    st.append("B2")
    st.append("F2")
    st.append("F'2")
    # 3's
    st.append("B3")
    st.append("F3")
    st.append("F'3")
    # 4's
    st.append("B4")
    # Rs
    st.append("R4")
    st.append("R'4")
    st.append("R3")
    st.append("R'3")
    st.append("R1")
    st.append("R'1")


    passes = []
    missing = st.copy()
    failures = []

    for i in range(len(states)):
        if states[i] in st:
            passes.append(states[i])
            missing.remove(states[i])
        elif not(states[i] in st):
            failures.append(states[i])

    print("Number Passed: ", len(passes), "Out of: ", len(st))
    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(st))
    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(st))
    for p in missing:
        print("Missing: ", p)

def affinities_test_14(aff_dict):
    #Hard Coded for N = 14
    st = []
    rs = []
    pr = []
    npr = []

    # S and 0s
    st.append("S")
    st.append("B0")
    npr.append("B0")
    st.append("B'0")
    pr.append("B'0")
    st.append("F0")
    npr.append("F0")
    # 1s
    st.append("B1")
    npr.append("B1")
    st.append("F1")
    npr.append("F1")
    st.append("F'1")
    pr.append("F'1")
    # 2s
    st.append("B2")
    npr.append("B2")
    st.append("F2")
    npr.append("F2")
    st.append("F'2")
    pr.append("F'2")
    # 3's
    st.append("B3")
    npr.append("B3")
    # Rs
    st.append("R3")
    npr.append("R3")
    st.append("R'3")
    pr.append("R'3")
    st.append("R2")
    npr.append("R2")
    st.append("R'2")
    pr.append("R'2")
    st.append("R'0")
    pr.append("R'0")

    rs.append("R3")
    rs.append("R'3")
    rs.append("R2")
    rs.append("R'2")
    rs.append("R'0")

    #Affs
    correct_affs = [[], [], [], [], []]
    aff_copy = aff_dict.copy()

    # Seed Affinities
    for n in npr:
        if n == "R2":
            pass
        else:
            correct_affs[0].append(("S", n))

    correct_affs[0].sort()
    print("Correct Seed Affinities: ")
    print(correct_affs[0])

    print("Current Seed Affinities: ")
    saffs = []
    for i in aff_copy:
        if i[0] == "S":
            saffs.append(i)
    print(saffs)

    # Attachments to self
    for n in npr:
        if n[1] == "0":
            pass
        elif n[1] == "1":
            pass
        else:
            correct_affs[1].append((n, n))

    print("Correct Self Attachment Affinities: ")
    print(correct_affs[1])

    print("Current Self Attachment Affinities: ")
    saffs = []
    for i in aff_copy:
        if i[0] == i[1]:
            saffs.append(i)
    print(saffs)

    # Attachments to prime self
    for n in npr:
        if n[1] == "0":
            pass
        elif n[0] == "B":
            pass
        else:
            l2 = make_prime(n)
            correct_affs[2].append((n, l2))

    print("Correct Self Prime Attachment Affinities: ")
    print(correct_affs[2])

    print("Current Self Prime Attachment Affinities: ")
    spaffs = []
    for i in aff_copy:
        if "'" not in i[0]:
            pv = i[0][0] + "'" + i[0][1:]
            if pv == i[1]:
                spaffs.append(i)
    print(spaffs)

    # Attachments to b0 f0
    for n in pr:
        if n == "B'0" or n == "R'0":
            pass

        else:
            correct_affs[3].append((n, "B0"))
            correct_affs[3].append((n, "F0"))

    print("Correct Prime b0 f0 Affinities: ")
    print(correct_affs[3])

    print("Current Prime b0 f0 Affinities: ")
    saffs = []
    for i in aff_copy:
        if i[0] in pr:
            if i[1][1:] == "0" or i[1][1:] == "1":
                saffs.append(i)
    print(saffs)


    # Test List
    all_affs =[("S", "B0"), ("S", "B1"), ("S", "B2"), ("S", "B3"),
               ("S", "F0"), ("S", "F1"), ("S", "F2"),
               ("S", "R3"),
               ("F0", "B0"),
               ("F'1", "B0"), ("F'2", "B0"), ("R'3", "B0"), ("R'2", "B0"),
               ("F'1", "F0"), ("F'2", "F0"), ("R'3", "F0"), ("R'2", "R'0"),
               ("F0", "B'0"), ("F1", "B'0"), ("F2", "B'0"), ("R2", "B'0"), ("R3", "B'0"),
               ("F'1", "B1"), ("F'2", "B1"), ("R'3", "B1"),
               ("F'2", "F1"), ("R'3", "F1"),
               ("F'2", "B2"), ("R'3", "B2"),
               ("R'3", "R2"),  ("F2", "B3"),
               ("F2", "F2"), ("B3", "B3"), ("B2", "B2"), ("F2", "F'2"), ("R2", "R2"), ("R3", "R3"),
               ("B1", "B'0"), ("F1", "F'1"), ("B2", "B1"),  ("F1", "B2"), ("F2", "B2"),("F2", "B1"), ("B3", "B2"), ("R3", "B3"), ("R3", "B2"), ("R3", "B1"), ("R3", "R'3"), ("R2", "B2"), ("R2", "B1"), ("R2", "R'2")]

    passes = []
    missing = all_affs.copy()
    failures = []
    all_affs.sort()
    j = 0
    for i in aff_copy:
        if i in all_affs:
            passes.append(i)
            missing.remove(i)
        else:
            failures.append(i)

    for i in missing:
        if i in failures:
            failures.remove(i)

    print("All affinities test:")
    print("Number Passed: ", len(passes), "Out of: ", len(all_affs))
    passes.sort()
    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(all_affs))
    failures.sort()
    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(all_affs))
    missing.sort()
    for p in missing:
        print("Missing: ", p)

def affinities_test_17(aff_dict):
    st = []
    pr = []
    npr = []
    # S and 0s
    st.append("S")
    st.append("B0")
    npr.append("B0")
    st.append("B'0")
    pr.append("B'0")
    st.append("F0")
    npr.append("F0")
    # 1s
    st.append("B1")
    npr.append("B1")
    st.append("F1")
    npr.append("F1")
    st.append("F'1")
    pr.append("F'1")
    # 2s
    st.append("B2")
    npr.append("B2")
    st.append("F2")
    npr.append("F2")
    st.append("F'2")
    pr.append("F'2")
    # 3's
    st.append("B3")
    npr.append("B3")
    st.append("F3")
    npr.append("F3")
    st.append("F'3")
    pr.append("F'3")
    # 4's
    st.append("B4")
    npr.append("B4")
    # Reseed
    st.append("R4")
    npr.append("R4")
    st.append("R'4")
    pr.append("R'4")

    all_affs =[("S", "B0"), ("S", "B1"), ("S", "B2"), ("S", "B3"), ("S", "B4"),
               # S forward
               ("S", "F0"), ("S", "F1"), ("S", "F2"), ("S", "F3"),

               # F0 B0
               ("F0", "B0"),
                # F' to B0
               ("F'1", "B0"), ("F'2", "B0"), ("F'3", "B0"),
               # F' to F0
               ("F'1", "F0"), ("F'2", "F0"), ("F'3", "F0"),
               #Fs to B'0
               ("F0", "B'0"), ("F1", "B'0"), ("F2", "B'0"), ("F3", "B'0"),
               # B1 to B'0
               ("B1", "B'0"),
               # F' to B1
               ("F'1", "B1"), ("F'2", "B1"), ("F'3", "B1"),
               #Fs to B1
               ("F2", "B1"), ("F3", "B1"),

               # F' to F1
               ("F'2", "F1"), ("F'3", "F1"), ("F'3", "F2"),


               #F1 to F'1
               # F' to B2
               ("F'2", "B2"), ("F'3", "B2"),
               # F' to B3
               ("F'3", "B3"),
               # Attach to self
               ("F2", "F2"), ("F3", "F3"), ("B4", "B4"), ("B3", "B3"), ("B2", "B2"),
               # Attach to prime self
               ("F3", "F'3"), ("F2", "F'2"), ("F1", "F'1"),
               # F to larger B
               ("F2", "B3"), ("F3", "B4"),  ("F1", "B2"),
               # B to smaller B
               ("B4","B3"), ("B3", "B2"), ("B2", "B1"),
               # F to smaller B
                ("F3", "B2"),
               # F to equal B
               ("F2", "B2"), ("F3", "B3"),
               # Reseed affinities
               ("S", "R4"), ("R4", "R'4"), ("R4", "R4"), ("R4", "B4"), ("R4", "B3"), ("R4", "B2"), ("R4", "B1"), ("R4", "B'0")
               ]

    aff_copy = aff_dict.copy()
    passes = []
    missing = all_affs.copy()
    failures = []
    all_affs.sort()
    j = 0
    for i in aff_copy:
        if i in all_affs:
            passes.append(i)
            missing.remove(i)
        else:
            failures.append(i)

    for i in missing:
        if i in failures:
            failures.remove(i)

    print("All affinities test:")
    print("Number Passed: ", len(passes), "Out of: ", len(all_affs))
    passes.sort()
    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(all_affs))
    failures.sort()
    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(all_affs))
    missing.sort()
    for p in missing:
        print("Missing: ", p)

# Test affinities for line of len 9
def affinities_test_9(aff_dict):
    st = []
    pr = []
    npr = []
    rs = []
    # S and 0s
    st.append("S")
    st.append("B0")
    npr.append("B0")
    st.append("B'0")
    pr.append("B'0")
    st.append("F0")
    npr.append("F0")
    # 1s
    st.append("B1")
    npr.append("B1")
    st.append("F1")
    npr.append("F1")
    st.append("F'1")
    pr.append("F'1")
    # 2s
    st.append("B2")
    npr.append("B2")
    st.append("F2")
    npr.append("F2")
    st.append("F'2")
    pr.append("F'2")
    # 3's
    st.append("B3")
    npr.append("B3")

    # Reseed
    rs.append("R3")
    rs.append("R'3")

    all_affs =[("S", "B0"), ("S", "B1"), ("S", "B2"), ("S", "B3"),
               # S forward
               ("S", "F0"), ("S", "F1"), ("S", "F2"), ("S", "R3"),
               # F0 B0
               ("F0", "B0"),
                # F' to B0
               ("F'1", "B0"), ("F'2", "B0"),
               # F' to F0
               ("F'1", "F0"), ("F'2", "F0"),
               #Fs to B'0
               ("F0", "B'0"), ("F1", "B'0"), ("F2", "B'0"), ("R3", "B'0"),
               # B1 to B'0
               ("B1", "B'0"),
               # F' to B1
               ("F'1", "B1"), ("F'2", "B1"),
               #Fs to B1
               ("F2", "B1"), ("R3", "B1"),

               # F' to F1
               ("F'2", "F1"),

               # F' to B2
               ("F'2", "B2"),
               # F' to B3
               ("F'3", "B3"),
               # Attach to self
               ("F2", "F2"),  ("B3", "B3"), ("B2", "B2"), ("R3", "R3"),
               # Attach to prime self
               ("F2", "F'2"), ("F1", "F'1"), ("R3", "R'3"),
               # F to larger B
               ("F2", "B3"), ("F1", "B2"),
               # B to smaller B
               ("B3", "B2"), ("B2", "B1"),
               # F to smaller B
               ("R3", "B2"),
               # FR to equal B
               ("F2", "B2"), ("R3", "B3"),


               ]

    aff_copy = aff_dict.copy()
    passes = []
    missing = all_affs.copy()
    failures = []
    all_affs.sort()
    j = 0
    for i in all_affs:
        if i in aff_copy:
            passes.append(i)
            missing.remove(i)
        else:
            failures.append(i)

    for i in missing:
        if i in failures:
            failures.remove(i)

    print("All affinities test:")
    print("Number Passed: ", len(passes), "Out of: ", len(all_affs))
    passes.sort()
    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(all_affs))
    failures.sort()
    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(all_affs))
    missing.sort()
    for p in missing:
        print("Missing: ", p)

def transition_rules_check_14(trans_dict):

    all_transitions = {
        ("S", "B0"):("S", "F0"),
        ("S", "B1"):("S", "F1"),
        ("S", "B2"):("S", "F2"),
        ("S", "B3"):("S", "R3"),
        ("F0", "B0"):("F0", "B'0"),
        ("F0", "B'0"):("B1", "B'0"),
        ("F1", "B'0"):("F1", "F'1"),
        ("F2", "B'0"):("F2", "F'2"),
        ("R3", "B'0"):("R3", "R'3"),
        ("R2", "B'0"):("R2", "R'2"),

        ("F2", "B2"):("F2", "F2"),
        ("F'1", "B1"):("B2", "B1"),

        ("F'2", "B2"):("B3", "B2"),
        ("F1", "B2"):("B2", "B2"),
        ("F2", "B3"):("B3", "B3"),
        ("F'1", "B0"):("F'1", "F0"),
        ("F'2", "B0"):("F'2", "F0"),
        ("F'2", "B1"):("F'2", "F1"),
        ("R'3", "B0"):("R'3", "F0"),
        ("R'3", "B1"):("R'3", "F1"),
        ("R'3", "B2"):("R'3", "R2"),
        ("R'2", "B0"):("R'2", "R'0"),

        ("R3", "B1"):("R3", "R3"),
        ("R3", "B2"):("R3", "R3"),
        ("R3", "B3"):("R3", "R3"),

        ("R2", "B2"):("R2", "R2"),
        ("R2", "B1"):("R2", "R2"),

        ("F2", "B1"):("F2", "F2"),


        }

    trans_copy = trans_dict.copy()
    passes = {}
    missing = all_transitions.copy()
    failures = {}

    j = 0
    for key in trans_copy:
        if key in all_transitions and (trans_copy[key] == all_transitions[key]):
            passes[key] = trans_copy[key]
            missing.pop(key)
        else:
            failures[key] = trans_copy[key]

    for key in missing:
        if key in failures:
            failures.pop(key)

    print("All transitions test:")
    print("Number Passed: ", len(passes), "Out of: ", len(all_transitions))

    for p in passes:
        print("Passed: ", p)

    print("Number Failed: ", len(failures), "Out of: ", len(all_transitions))

    for p in failures:
        print("Failed: ", p)

    print("Number Missing: ", len(missing), "Out of: ", len(all_transitions))

    for p in missing:
        print("Missing: ", p)