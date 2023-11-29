import csv
import matplotlib.pyplot as plt
import statistics
    
def main():
    file_path = "CF_DATA.txt"
    with open(file_path, 'r') as file:
    
        csv_reader = csv.reader(file)
        data_array = [row for row in csv_reader]

        #find mean time per task

    login_mean = 0
    profile_mean = 0
    home_mean = 0
    quiz_mean = 0
    chat_mean = 0
    education_mean = 0
    help_mean = 0
    settings_mean = 0
    career_mean = 0

    login_std = []
    profile_std = []
    home_std = []
    quiz_std = []
    chat_std = []
    education_std = []
    help_std = []
    settings_std = []
    career_std = []

    i = 0
    for row in data_array:
        if data_array[i][0] == "Login":
            login_mean += float(data_array[i][1])
            login_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Profile/pinned career":
            profile_mean += float(data_array[i][1])
            profile_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Navigate home":
            home_mean += float(data_array[i][1])
            home_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Quiz page 2":
            quiz_mean += float(data_array[i][1])
            quiz_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Professional chat":
            chat_mean += float(data_array[i][1])
            chat_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Education search":
            education_mean += float(data_array[i][1])
            education_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Help search":
            help_mean += float(data_array[i][1])
            help_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Navigate settings":
            settings_mean += float(data_array[i][1])
            settings_std.append(float(data_array[i][1]))
        if data_array[i][0] == "Career search":
            career_mean += float(data_array[i][1])
            career_std.append(float(data_array[i][1]))
        i += 1

    login_mean = login_mean/5
    profile_mean = profile_mean/5
    home_mean = home_mean/5
    quiz_mean = quiz_mean/5
    chat_mean = chat_mean/5
    education_mean = education_mean/5
    help_mean = help_mean/5
    settings_mean = settings_mean/5
    career_mean = career_mean/5

    

    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()

    mean_labels = ["Login", "Profile", "Home", "Quiz", "Chat", "Education", "Help", "Settings", "Career"]
    time_means = [login_mean,profile_mean,home_mean,quiz_mean,chat_mean,education_mean,help_mean,settings_mean,career_mean ]
    bar_colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple', 'pink', 'black', 'brown']

    ax.bar(mean_labels, time_means, color=bar_colors)

    ax.set_ylabel('Mean Seconds')
    ax.set_title('Tasks by mean seconds')
    ax.legend(title='')

    #-----------

    # (statistics.stdev(sample))

    login_std = (statistics.stdev(login_std))
    profile_std = (statistics.stdev(profile_std))
    home_std = (statistics.stdev(home_std))
    quiz_std = (statistics.stdev(quiz_std))
    chat_std = (statistics.stdev(chat_std))
    education_std = (statistics.stdev(education_std))
    help_std = (statistics.stdev(help_std))
    settings_std = (statistics.stdev(settings_std))
    career_std = (statistics.stdev(career_std))

    task_labels = ["Login", "Profile", "Home", "Quiz", "Chat", "Education", "Help", "Settings", "Career"]
    task_std = [login_std,profile_std,home_std,quiz_std,chat_std,education_std,help_std,settings_std,career_std ]
    bar_colors2 = ['red', 'blue', 'yellow', 'orange', 'green', 'purple', 'pink', 'black', 'brown']

    ax2.bar(task_labels, task_std, color=bar_colors2)

    
    ax2.set_ylabel('Standard deviation')
    ax2.set_title('Tasks by standard deviation')
    ax2.legend(title='')

    plt.show()


main()