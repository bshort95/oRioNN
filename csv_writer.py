import csv

def csv_writer(list):
    filename = "output/dummy_data.csv"
    
    fields = ["Score (Average Rating)", "Score (Outcome Average)", "Score (Caregiver's Average)",
    "Score (Office Staff Average)", "Comment (Likely to recommend)", "Score (Likely to recommend)",
    "Comment (Impact of service)", "Score (Impact of service)",
    "Comment (Caregiver ability)", "Score (Caregiver ability)",
    "Comment (Communication and helpfulness)", "Score (Communication and helpfulness)",
    "Comment (Needs and preferences)", "Score (Needs and preferences)",
    "Comment (How to improve)", "Comment (Consent for marketing)"]
    
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        for item in list:
            csv_writer.writerow(item)


# Testing
# list = [[6, 7, 8, 9, "Yes it is great!", 6, "Makes life easier", 7, "They were very caring", 8, "They answered questions", 9, "They were on top of things", 10, "Nothing at the moment", "No"],
# [8, 7, 8, 9, "Yes, we enjoy the service.", 8, "Helps our routine go smooth", 9, "Good sense of humor", 8, "Great attention to detail", 7, "Very smart folks", 9, "Earlier call ahead", "Yes"]]
# csv_writer(list)