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
