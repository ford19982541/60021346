'''
proc = []
a = []
b = []
c = []
d = []

name = str(input("name :"))
a.append(name)
wt = input("wt :")
a.append(wt)
at = int(input("at :"))
a.append(at)

name = str(input("name :"))
b.append(name)
wt = input("wt :")
b.append(wt)
at = int(input("at :"))
b.append(at)

name = str(input("name :"))
c.append(name)
wt = input("wt :")
c.append(wt)
at = int(input("at :"))
c.append(at)

name = str(input("name :"))
d.append(name)
wt = input("wt :")
d.append(wt)
at = int(input("at :"))
d.append(at)

proc.append(a)
proc.append(b)
proc.append(c)
proc.append(d)
print(proc)
def sort(proc):
    for i in range(len(proc)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(proc[i[2]])):
            if proc[min_idx[2]] > proc[j[2]]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        proc[i],proc[min_idx] = proc[min_idx], proc[i]

print("sort :",proc)
'''
input_list = []
qq = []
wait_q_name = []


def filter_input(p, c, t):
    input_dict = {"process_id":p,"cpu_cycle":c,"create_time": t}
    if (len(input_list) != 0):
        for i in range(len(input_list)):
            if (t == input_list[i]["create_time"]):
                if (c < input_list[i]["cpu_cycle"]):
                    input_list.insert(i, input_dict)
                    break
                else:
                    if (len(input_list) == i + 1):
                        input_list.append(input_dict)
                        break
                    else:
                        input_list.insert(i + 1, input_dict)
                        break
            elif (t < input_list[i]["create_time"]):
                input_list.insert(i, input_dict)
                break
        else:
            input_list.append(input_dict)

    else:
        input_list.append({"process_id":p, "cpu_cycle": c, "create_time": t})

        def sortqq(l):
            nl = []
            if (len(l) <= 1):
                nl = l
            else:
                for i in range(len(l)):
                    for j in range(len(l) - 1):
                        if l[j]["cpu_cycle"] > l[j + 1]["cpu_cycle"]:
                            l[j], l[j + 1] = l[j + 1], l[j]
                nl = l
            # print("insortqq",nl)
            return nl

        def check_create_item(p):
            q = []
            for i in range(len(input_list)):
                if input_list[i]["create_time"] == p:
                    wait_q_name.append(input_list[i]["process_id"])
                    input_list[i]["come"] = p
                    q.append(input_list[i])
            qq = q
            return qq

        while True:
            processID = input("กรุณากรอกโปรเซสไอดี กรอก 0 เพื่อจบการกรอกข้อมูล :").strip()
            if (processID == "0"):
                break
            cpu_cycle = int(input("กรุณากรอก  ซีพียูไซเคิล :"))
            createTime = int(input("กรุณากรอก เวลาเริ่มต้น :"))
            filter_input(processID, cpu_cycle, createTime)
            print("-" * 40)

        # for i in range(len(input_list)):
        # print(input_list[i])
        print("      CPU_Cycle \t Process")
        processed_list = []
        q_process = []
        cpu_process = 0
        while (len(processed_list) < len(input_list)):
            # เริ่มทำงาน
            q = check_create_item(cpu_process)
            if (q != []):
                if (type(q) == type([])):
                    qq += q
                else:
                    qq.append(q)
                    # print(cpu_process,qq)
            qq = sortqq(qq)
            if (len(qq) != 0):
                qq[0]["start"] = cpu_process
                wait_q_name.remove(qq[0]["process_id"])
                for i in range(qq[0]["cpu_cycle"]):  # เเสดง ตาม cpu_cycle
                    print("\t", cpu_process, "\t\t    ",
                          qq[0]["process_id"] + " " + str((wait_q_name) if wait_q_name != [] else ""))
                    cpu_process += 1

                    q = check_create_item(cpu_process)
                    if (q != []):
                        if (type(q) == type([])):
                            qq += q
                        else:
                            qq.append(q)
                            # print(cpu_process,qq)
                qq[0]["out"] = cpu_process
                processed_list.append(qq[0])
                qq.remove(qq[0])
            else:
                print("\t", cpu_process)
                cpu_process += 1

        # print(processed_list)

        TRT = 0
        WTT = 0
        for i in range(len(processed_list)):
            TRT += abs(processed_list[i]["out"] - processed_list[i]["come"])
            WTT += abs(processed_list[i]["come"] - processed_list[i]["start"])
        # print(processed_list)


        avg_turnaround_time = TRT / len(processed_list)
        avg_waitting_time = WTT / len(processed_list)
        print("-" * 40)
        print("avg waitting time", avg_waitting_time)
        print("avg turnaround time", avg_turnaround_time)