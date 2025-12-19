# todo.py - 支持删除功能的待办事项管理器
import sys

todos = []

def show_help():
    print("用法:")
    print("  python todo.py add <事项内容>     # 添加待办")
    print("  python todo.py list               # 列出所有待办")
    print("  python todo.py delete <序号>      # 删除指定序号的待办")
    print("  python todo.py help               # 显示帮助")

def add_todo(task):
    todos.append(task)
    print(f"✅ 已添加: {task}")

def list_todos():
    if not todos:
        print("📝 暂无待办事项")
    else:
        print("📝 待办列表:")
        for i, t in enumerate(todos, 1):
            print(f"  {i}. {t}")

def delete_todo(index_str):
    try:
        idx = int(index_str) - 1  # 用户输入从1开始
        if idx < 0 or idx >= len(todos):
            print("❌ 序号超出范围")
            return
        removed = todos.pop(idx)
        print(f"🗑️ 已删除: {removed}")
    except ValueError:
        print("❌ 请输入有效的数字序号")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        show_help()
    elif command == "add":
        if len(sys.argv) < 3:
            print("❌ 请提供待办事项内容")
        else:
            task = " ".join(sys.argv[2:])
            add_todo(task)
    elif command == "list":
        list_todos()
    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ 请提供要删除的序号")
        else:
            delete_todo(sys.argv[2])
    else:
        print(f"❌ 未知命令: {command}")
        show_help()