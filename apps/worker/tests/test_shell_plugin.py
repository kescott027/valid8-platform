from worker.plugins.shell import ShellPlugin


def test_shell_plugin_runs_echo(tmp_path):
  plugin = ShellPlugin()
  res = plugin.run({"type": "shell", "cmd": ["echo", "hello"]}, workdir=str(tmp_path))
  assert res.ok is True
  assert any("hello" in line for line in res.logs)
