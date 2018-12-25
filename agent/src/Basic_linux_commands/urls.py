from Basic_linux_commands.linux_commands import cmd_home, list_dir, make_dir, archive, extract, kill, copy_files, move_files, remove_files, change_owner, change_mode, head, tail

path = {
    '/': cmd_home,
    '/ls/': list_dir,
    '/mkdir/': make_dir,
    '/archive/': archive,
    '/extract/': extract,
    '/kill/': kill,
    '/copy/': copy_files,
    '/move/': move_files,
    '/remove/': remove_files,
    'chown/': change_owner,
    '/chmod/': change_mode,
    '/head/': head,
    '/tail/': tail,
}
