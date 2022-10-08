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
