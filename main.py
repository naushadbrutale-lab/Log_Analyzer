from analyzer import read_logs, parse_logs, generate_report

def main():
    file_path = "sample.log"

    logs = read_logs(file_path)
    print("Logs loaded:", logs)

    parsed_logs = parse_logs(logs)
    print("Parsed logs:", parsed_logs)

    generate_report(parsed_logs)

if __name__ == "__main__":
    main()