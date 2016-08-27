/**
 * Created by dharmendra on 25/8/16.
 */

var my_app = angular.module('MyApp').config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
