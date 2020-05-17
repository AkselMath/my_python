import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"

football = pd.read_csv(url)

# задание 1
print(round(football.Age.mean()))

# задание 2
print(football.Composure.count())

# задание 3
print(round(football.ShortPassing.std()), 2)

# задание 4
print(round(football.Wage.sum()))

# задание 5
print(round(football.Value.min()))

# задание 1
print(
    round(football[football.Wage > football.Wage.mean()].SprintSpeed.mean(), 2)
)

# задание 2
print(
    round(football[football.Wage < football.Wage.mean()].SprintSpeed.mean(), 2)
)

# задание 3
print(
    football[football.Wage == football.Wage.max()]["Position"]
)

# задание 4
print(
    football[football.Nationality == "Brazil"].Penalties.sum()
)

# задание 5
print(
    round(football[football.HeadingAccuracy > 50].Age.mean(), 2)
)

# задание 6
a = football[(football.Composure > 90) & (football.Reactions > 90)]
print(a[a.Age == a.Age.min()]["Name"])

# задание 7
print(
    round(football[football.Age == football.Age.max()].Reactions.mean() -
          football[football.Age == football.Age.min()].Reactions.mean(), 2)
)

# задание 8
print(football[football.Value > football.Value.mean()].Nationality.value_counts())

# задание 9
print(
    round(
    football[(football.Position == "GK") & (football.GKReflexes == football.GKReflexes.max())].Wage.mean()/
    football[(football.Position == "GK") & (football.GKHandling == football.GKHandling.max())].Wage.mean(),
        2
        )
    )

# задание 10
print(
    round(
    football[(football.Aggression == football.Aggression.max())].ShotPower.mean() /
    football[(football.Aggression == football.Aggression.min())].ShotPower.mean(),
        2
        )
    )
