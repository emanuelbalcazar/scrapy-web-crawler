module.exports = function (grunt) {

    require('time-grunt')(grunt);
    grunt.loadNpmTasks('grunt-shell');

    // task configuration will be written here.
    grunt.initConfig({
        package: grunt.file.readJSON('package.json'),
        
        // execute shell commands
        shell: {
            options: {
                stdout: true
            },
            freeze: {
                command: 'pip3 freeze > requirements.txt'
            },
            install: {
                command: 'pip3 install -r requirements.txt'
            },
            crawl: {
                command: 'scrapy crawl crawler -o logs/links-traveled.log -t csv'
            }
        }
    });

    // register all tasks.
    grunt.registerTask('default', ['shell:crawl']);
    grunt.registerTask('freeze', ['shell:freeze']);
    grunt.registerTask('install', ['shell:install']);
    grunt.registerTask('crawl', ['shell:crawl']);
};