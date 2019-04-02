CONFIG = {                                                                      
    'mode': 'wsgi',                                                           
    'working_dir': '/home/box/web',                                           
    'python': '/usr/bin/python3',                                              
    'args': (                                                                   
        '--bind=0.0.0.0:8000',                                              
        '--workers=2',                                                         
        '--timeout=30',                                                         
        'hello:app',                                                           
    ),                                                                          
} 