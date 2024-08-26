import json

from attack import Attack
from robot import Robot, Team
from skill import Skill


def load_opponents(opponents_data):
    opponents = []
    for opponent in opponents_data:
        if opponent == "teams":
            opponents = opponents + load_teams(opponents_data["teams"])

        elif opponent == "robots":
            opponents = opponents + load_robots(opponents_data["robots"])
    return opponents


def load_file(file_name: str):
    with open(file_name, "r") as f:
        return json.load(f)


def load_teams(teams_data: list[dict]) -> list[Team]:
    teams = []
    for team_dict in teams_data:
        teams.append(
            Team(name=team_dict["name"], teammates=load_robots(team_dict["robots"]))
        )
    return teams


def load_robots(robots_data: list[dict]) -> list[Robot]:
    robots = []
    for robot_dict in robots_data:
        robots.append(
            Robot(
                name=robot_dict["name"],
                energy=robot_dict["energy"],
                attacks=load_attacks(robot_dict["attacks"]),
                skills=load_skills(robot_dict["skills"]),
            )
        )
    return robots


def load_attacks(attacks_data: list[dict]) -> list[Attack]:
    attacks = []
    for attack_dict in attacks_data:
        attacks.append(
            Attack(
                name=attack_dict["name"],
                type=attack_dict["type"],
                objetive=attack_dict["objetive"],
                damage=attack_dict["damage"],
                precision=attack_dict["precision"],
                recharge=attack_dict["recharge"],
            )
        )
    return attacks


def load_skills(skills_data: list[dict]) -> list[Skill]:
    skills = []
    for skill_dict in skills_data:
        skills.append(
            Skill(
                name=skill_dict["name"],
                trigger=skill_dict["trigger"],
                trigger_value=skill_dict["trigger_value"],
                duration=skill_dict["duration"],
                objective=skill_dict["objetive"],
                effect=skill_dict["effect"],
                effect_value=skill_dict["effect_value"],
            )
        )
    return skills


if __name__ == "__main__":
    print(load_file("./robots.json"))
    load_robots(load_file("./robots.json")["robots"])
