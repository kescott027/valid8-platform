from worker.registry import PluginRegistry


def test_registry_has_shell():
  reg = PluginRegistry.default()
  assert reg.get("shell").kind == "shell"
