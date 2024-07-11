# Sets up your web servers for deployment
exec { 'update_apt':
  command => '/usr/bin/env apt-get -y update',
}
-> exec { 'install_nginx':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec { 'add_rewrite_rule':
  command => '/usr/bin/env sed -i "/listen \[::\]:80 default_server/ a\\\trewrite ^/redirect_me http://www.holbertonschool.com permanent;" /etc/nginx/sites-available/default',
}
-> exec { 'add_header':
  command => '/usr/bin/env sed -i "/listen \[::\]:80 default_server/ a\\\tadd_header X-Served-By \"\$HOSTNAME\";" /etc/nginx/sites-available/default',
}
-> exec { 'add_custom_404':
  command => '/usr/bin/env sed -i "/redirect_me/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default',
}
-> exec { 'create_404_page':
  command => '/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html',
}
-> exec { 'start_nginx':
  command => '/usr/bin/env service nginx start',
}
-> exec { 'create_release_directory':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec { 'create_shared_directory':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec { 'create_test_index':
  command => '/usr/bin/env echo "Hello Holberton School!" > /data/web_static/releases/test/index.html',
}
-> exec { 'create_symlink':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'configure_nginx':
  command => '/usr/bin/env sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default',
}
-> exec { 'restart_nginx':
  command => '/usr/bin/env service nginx restart',
}
-> exec { 'set_permissions':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data/',
}
