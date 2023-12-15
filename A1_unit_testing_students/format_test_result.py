def test_format_regtest(read_file, write_file):
    # resets file
    with open(write_file, "w") as regtest:
        regtest.write("")
    # name of log file
    with open(read_file, "r") as file:
        lines = file.readlines()
        count_failed = 0
        count_passed = 0
        for line in lines:
            sum = "Test called "
            if line.__contains__("PASSED"):
                count_passed += 1
                splits = line.split()
                for splitted in splits:
                    if splitted.__contains__("name"):
                        sum += splitted.split('\'')[1]
                sum += " passed\n"
                print(sum)
                with open(write_file, "a") as regtest:
                    regtest.write(sum)
            elif line.__contains__("FAILED"):
                count_failed += 1
                splits = line.split()
                print(splits)
                for splitted in splits:
                    print(splitted)
                    if splitted.__contains__("name") and (not splitted.__contains__("|")) and (not splitted.__contains__(":")):
                        sum += splitted.split('\'')[1]
                sum += " failed\n"
                print(sum)
                with open(write_file, "a") as regtest:
                    regtest.write(sum)

        total = count_passed + count_failed

        with open(write_file, "a") as regtest:
            regtest.write("Total tests = " + str(total) + "\n")
            regtest.write("Total passed = " + str(count_passed) + "\n")
            regtest.write("Total failed = " + str(count_failed) + "\n")
            regtest.write("Pass rate = " + str((count_passed / total)*100) + "%\n")

        print("Total tests = " + str(total))
        print("Total passed = " + str(count_passed))
        print("Total failed = " + str(count_failed))
        print("Pass rate = " + str((count_passed / total)*100) + "%")

read_file = "unformatted_logfile2.txt"
write_file = "logfile2.txt"
test_format_regtest(write_file=write_file, read_file=read_file)