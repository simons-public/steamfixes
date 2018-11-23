project('steamfixes', ['c'])

loader_args = []
if get_option('buildtype') == 'debug'
  loader_args += '-DDEBUG'
endif

loader_full_path = join_paths(get_option('prefix'), get_option('bindir'), 'steamfixes')
loader_args += '-DLOADER="' + loader_full_path + '"'

shared_library('loader', 'src/loader.c',
  c_args      : loader_args,
  link_args   : ['-ldl'],
  name_prefix : '',
  install_dir : join_paths(get_option('libdir'), 'steamfixes'),
  install     : true)

configure_file(copy: true,
  input       : files('src/steamfixes'),
  output      : 'steamfixes',
  install_dir : get_option('bindir'))


# Install steamfixes Python module
pymod = import('python')
py_installation = pymod.find_installation('python3')

py_files = files([
  'steamfixes/__init__.py',
  'steamfixes/fix.py',
  'steamfixes/game.py',
  'steamfixes/logger.py',
  'steamfixes/util.py',
])
py_installation.install_sources(py_files, subdir: 'steamfixes')


py_gamefixes_files = files([
  'steamfixes/gamefixes/200710.py'
])
py_installation.install_sources(py_gamefixes_files, subdir: 'steamfixes/gamefixes')
