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
                command: 'echo "\nGenerando requirements.txt\n" && pip3 freeze > requirements.txt'
            },
            install: {
                command: 'echo "\nInstalando dependencias:\n" && pip3 install -r requirements.txt'
            },
            crawl: {
                command: 'echo "\nIniciando ejecucion:\n" && scrapy crawl google.news'
            },
            list: {
                command: 'echo "\nSpiders disponibles:\n" && scrapy list'
            },
            check: {
                command: 'echo "\nRevisando la correctitud de los spiders:\n" && scrapy check'
            }
        }
    });

    // register all tasks.
    grunt.registerTask('default', ['shell:crawl']);
    grunt.registerTask('freeze', ['shell:freeze']);
    grunt.registerTask('install', ['shell:install']);
    grunt.registerTask('crawl', ['shell:crawl']);
    grunt.registerTask('list', ['shell:list']);
    grunt.registerTask('check', ['shell:check']);
};