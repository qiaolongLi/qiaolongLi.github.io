import pandas as pd
import datetime

def to_css(a_time):
    if type(a_time) != str:
        return ""
    if len(a_time) == 4:
        a_time = "0" + a_time.replace(":","")
    else:
        a_time = a_time.replace(":","")
    return a_time

def get_authors(talk):
    authors = ""
    n_speakers = 3
    col_str = "Speaker #{0} Name"
    aff_str = "Speaker #{0} Affiliation"
    for i in range(1,n_speakers):
        if not pd.isna(talk[col_str.format(i)]):
            authors += "\n\t\t\t\t" + talk[col_str.format(i)] 
            if not pd.isna(talk[aff_str.format(i)]):
                authors += " ({0})".format(talk[aff_str.format(i)])
            authors += "<br>"
    
    #authors = authors[] # remove last comma
    if len(authors) > 0:
        authors = authors[:-4]
    return authors
        
def make_full_track(talk,session):
    start = talk["Presentation Start Time"]
    stop = talk["Presentation End Time"]
    authors = get_authors(talk)
    output = ""
    output += '\t<h2 class="time-slot" style="grid-row: time-{0};">{1} JST</h2>\n\n'.format(to_css(start),start)
    output += '\t<div class="session session-{0} track-all" style="grid-column: track-1-start / track-2-end; grid-row: time-{1} / time-{2};">\n'.format(session,to_css(start),to_css(stop))
    output += '\t\t<h3 class="session-title">{0}</h3>\n'.format(talk["Presentation Title"])
    output += '\t\t<br>\n'
    if not pd.isna(talk["Track Title"]):
        output += '\t\t<span class="session-track">{0} </span>\n'.format(talk["Track Title"])

    output += '\t\t<h3 class="session-presenter">{0}\n\t\t</h3>\n'.format(authors)
    output += '\t\t<h3 class="session-presenter">New Hall\n\t\t</h3>\n'
    if not pd.isna(talk["Summary"]):
        output += '\t\t<br>'
        output += '\t\t<span class="session-description">{0}</span>\n'.format(talk["Summary"])

    output += '\t\t<br>\n'
    links = "Relevant Links from Submission"
    if not pd.isna(talk[links]):        
        link = talk[links].split("\n")[0]
        output += '\t\t<br>\n'
        output += '\t\t<a href="{0}" target="_blank" class="video-link">🌐 More Info</a>\n'.format(link)

    if not pd.isna(talk["Video URL"]):
         output += '\t\t<br>\n'
         output += '\t\t<a href="{0}" target="_blank" class="video-link">📹 Watch </a>\n'.format(talk["Video URL"])

    if not pd.isna(talk["PDF Name"]):
        output += '\t\t<br>\n'
        output += '\t\t<a href="http://example.com/downloads/rosconxx/20XX/{0}" class="video-link">🗒️ Slides</a>\n'.format(talk['PDF Name'])

    output += '\t</div>\n\n'    
    return output


def make_track1(talk,session):

    output = ""

    start = talk["Presentation Start Time"]
    stop = talk["Presentation End Time"]
    authors = get_authors(talk)
    

    output += '\t<h2 class="time-slot" style="grid-row: time-{0};">{1} JST</h2>\n'.format(to_css(start),start)
    output += '\t<div class="session session-{0} track-1" style="grid-column: track-1; grid-row: time-{1} / time-{2};">\n'.format(session,to_css(start),to_css(stop))
    output += '\t\t<h3 class="session-title">{0}</h3>\n'.format(talk["Presentation Title"])

    if not pd.isna(talk["Track Title"]):
        output += '\t\t<span class="session-track">{0} </span>\n'.format(talk["Track Title"])

    output += '\t\t<span class="session-time">{0} - {1} JST</span>\n'.format(start,stop)
    output += '\t\t<br>\n'
    output += '\t\t<h3 class="session-presenter">{0}\n\t\t</h3>\n'.format(authors)
    output += '\t\t<h3 class="session-presenter">New Hall\n\t\t</h3>\n'

    if not pd.isna(talk["Summary"]):
        output += '\t\t<br>'
        output += '\t\t<span class="session-description">{0}</span>\n'.format(talk["Summary"])

    links = "Relevant Links from Submission"
    if not pd.isna(talk[links]):        
        link = talk[links].split("\n")[0]
        output += '\t\t<br>\n'
        output += '\t\t<a href="{0}" target="_blank" style="color:white" class="video-link">🌐 More Info</a>\n'.format(link)

    if not pd.isna(talk["Video URL"]):
         output += '\t\t<br>\n'
         output += '\t\t<a href="{0}" style="color:white" target="_blank" class="video-link">📹 Watch </a>\n'.format(talk["Video URL"])

    if not pd.isna(talk["PDF Name"]):
        output += '\t\t<br>\n'
        output += '\t\t<a href="http://example.com/downloads/rosconxx/20XX/{0}" class="video-link" style="color:white">🗒️ Slides</a>\n'.format(talk['PDF Name'])
        
    output += '\t</div>\n\n'
    return output



def make_track2(talk,session):
    output = ""

    start = talk["Presentation Start Time"]
    stop = talk["Presentation End Time"]
    authors = get_authors(talk)

    output += '\t<div class="session session-{0} track-2" style="grid-column: track-2; grid-row: time-{1} / time-{2};">\n'.format(session,to_css(start),to_css(stop))
    output += '\t\t<h3 class="session-title">{0}</h3>\n'.format(talk["Presentation Title"])

    if not pd.isna(talk["Track Title"]):
        output += '\t\t<span class="session-track">{0} </span>\n'.format(talk["Track Title"])

    
    output += '\t\t<span class="session-time">{0} - {1} JST</span>\n'.format(start,stop)
    output += '\t\t<br>\n'
    output += '\t\t<h3 class="session-presenter">{0}\n\t\t</h3>\n'.format(authors)
    output += '\t\t<h3 class="session-presenter">Annex\n\t\t</h3>\n'
    if not pd.isna(talk["Summary"]):
        output += '\t\t<br>'
        output += '\t\t<span class="session-description">{0}</span>\n'.format(talk["Summary"])
    links = "Relevant Links from Submission"
    if not pd.isna(talk[links]):        
        link = talk[links].split("\n")[0]
        output += '\t\t<br>\n'
        output += '\t\t<a href="{0}" target="_blank" style="color:white" class="video-link">🌐 More Info</a>\n'.format(link)

    if not pd.isna(talk["Video URL"]):
         output += '\t\t<br>\n'
         output += '\t\t<a href="{0}" style="color:white" target="_blank" class="video-link">📹 Watch </a>\n'.format(talk["Video URL"])

    if not pd.isna(talk["PDF Name"]):
        output += '\t\t<br>\n'
        output += '\t\t<a href="http://example.com/downloads/rosconxx/20XX/{0}" class="video-link" style="color:white">🗒️ Slides</a>\n'.format(talk['PDF Name'])
    output += '\t</div>\n\n'
    return output



def make_day(csv, day_string=""):
    output = ""
    preamble = """
<div class="schedule" aria-labelledby="schedule-heading">
\t<span class="track-slot" aria-hidden="true" style="grid-column: track-1; grid-row: tracks;">Track 1</span>
\t<span class="track-slot" aria-hidden="true" style="grid-column: track-2; grid-row: tracks;">Track 2</span>\n"""
    postamble = """
</div>
    """
    output += "\n<br>\n<H1> Day {0}  </H1>\n<br>".format(day_string)
    output += "\n<br>\n<H3> All times are Japan Standard Time (UTC+9) </H3>\n<br>"
    output += preamble
    start_t = "Presentation Start Time"
    track = "Track"

    # In theory this should work
    day = csv.copy()
    #day = day[day[start_t].notna()]
    
    day["start_int"] = day[start_t].tolist()

    day["start_int"] = day["start_int"].apply(lambda x: datetime.datetime.strptime(str(x), "%H:%M"))
    
    
    day = day.sort_values(by=["start_int","Track"])
    
    # Need to convert start_t to a usable value 

    #bprint(day[[start_t,"Presentation Title"]])
    session = 1

    
    for row in day.iterrows():
        talk = row[1]
        if talk["Track"] == 0:
            output += make_full_track(talk,session)
        elif talk["Track"] == 1:
            output += make_track1(talk,session)
        else:
            output += make_track2(talk,session)
        session += 1
    output += postamble
    return output

            

if __name__ == "__main__":
    # Spreadsheet is at:
    # https://docs.google.com/spreadsheets/d/19QoWA-dk2TPwVKJ93Yj0Lw1zkAzOOc73-jZMkkOeV0k/edit?usp=sharing

    # To run, copy spreadsheet to schedule_csv
    # run: python3 MakeROSConSchedule.py > ../_posts/2000-01-06-program.md 
    schedule_csv = "2022TalkSchedule.csv"
    output = "../_posts/2000-01-06-program.md"
    workshops = "./workshops.stub"
    
    schedule = pd.read_csv(schedule_csv)
    # Drop the first line
    schedule.drop(index=0,inplace=True)


    
    sd = "Session Date"
    days = schedule[sd].unique()

    
    # Break down the sessions by days
    day1 = schedule[schedule[sd]==days[1]]
    day2 = schedule[schedule[sd]==days[2]]

    # Print it all out 
    output = ""
    output += make_day(day1, "One, October 20th, 2022")
    output += make_day(day2, "Two, October 21st, 2022")

    with open(workshops,'r') as f:
        print(f.read())
    print(output)
