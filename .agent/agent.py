import os
import yaml
import json
from datetime import datetime

class AgentMemory:
    root = ".agent_memory"

    @staticmethod
    def save_context(filename, data):
        path = os.path.join(AgentMemory.root, filename)
        with open(path, "a") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    @staticmethod
    def load_context(filename):
        path = os.path.join(AgentMemory.root, filename)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return [json.loads(line) for line in f]

class SkillManager:
    root = ".agent_skills"

    @staticmethod
    def list_skills():
        return [
            d for d in os.listdir(SkillManager.root)
            if os.path.isdir(os.path.join(SkillManager.root, d))
            and os.path.exists(os.path.join(SkillManager.root, d, "skill.yaml"))
        ]
    
    @staticmethod
    def load_skill_desc(name):
        with open(os.path.join(SkillManager.root, name, "skill.yaml"), "r") as f:
            return yaml.safe_load(f)

def main():
    print("Available skills:")
    for s in SkillManager.list_skills():
        print(f" - {s}", SkillManager.load_skill_desc(s).get("description"))

    memos = AgentMemory.load_context("goals.yaml")
    print("Current goals:", memos)

if __name__ == "__main__":
    main()
