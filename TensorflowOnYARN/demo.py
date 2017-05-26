import json
import subprocess
import sys

# Example:
#   python demo.py "bin/ydl-tf" "launch" "examples/between-graph/mnist_feed.py"

def main():
  args = sys.argv[1:]
  output = subprocess.check_output([args[0], args[1]])
  # Typical output
  #   ClusterSpec: {"ps":["node13-3:22969"],"worker":["node13-3:22965","node13-1:22967"]}
  cluster_spec = json.loads(output.split(' ')[1])
  subprocess.call(["python", args[2], "--ps_hosts=" + ','.join(cluster_spec['ps']), "--worker_hosts=" + ','.join(cluster_spec['worker']), "--task_index=" + "0"])

if __name__ == "__main__":
  main()
