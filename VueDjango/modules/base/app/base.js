import Vue from 'vue'
import VueResource from 'vue-resource'


var cookieToolbox = function(){
    var set = function (name, value, days) {
        var d = new Date();
        d.setTime(d.getTime() + 24*60*60*1000*days);
        window.document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
    };

    var get = function (name) {
        var v = window.document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return v ? v[2] : null;
    };

    var deleteCookie = function (name) {
        set(name, '', -1);
    }
    return {
        set: set,
        get: get,
        deleteCookie: deleteCookie
    }
}

Vue.use(VueResource);
Vue.http.options.emulateJSON = true;
Vue.http.headers.common['X-CSRF-TOKEN'] = cookieToolbox().get(window.globalConfig.csrftokenName)


module.exports = {
	Vue: Vue,
	cookieToolbox: cookieToolbox()
}