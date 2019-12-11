from bs4 import BeautifulSoup

with open("./temp_text.html", "r", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, "html.parser")

    output = []


    ## 职位名称
    job_name = soup.select_one("#main > div.job-banner > div > div > div.info-primary > div.name > h1")
    output.append("|"+job_name.text+"|["+job_name.text+"]()")

    jd = soup.select_one("#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-child(1) > div")

    #print(jd.text.split("。"))
    ## 工作职责
    jb_1 = ""
    i = 0
    for one in jd.text.replace('\n','').split("。"):

        if "：" in one and i ==0:
            i = 1
        elif "：" in one and i != 0:
            break

        jb_1 += one.strip() + "<br>"

    output.append(jb_1)
    ## 岗位职责
    jb_2 = ""
    i = 0
    for one in jd.text.replace('\n','').split("。"):

        if "：" in one and i ==0:
            i = 1
        elif "：" in one and i != 0:
            i = 2
        if i == 2:
            jb_2 += one.strip() + "<br>"

    output.append(jb_2)

    ## 发布人
    publisher = soup.select_one("#main > div.job-box > div > div.job-detail > div.detail-op > h2")
    ## 发布人职位
    publisher_position = soup.select_one("#main > div.job-box > div > div.job-detail > div.detail-op > p")
    output.append(publisher.text +"<br>"+ publisher_position.text+"|")


print("|".join(output))