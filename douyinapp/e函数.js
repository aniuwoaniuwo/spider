function(t) {
    function e(t, e) {
        return e = e.charAt(0).toUpperCase() + e.slice(1),
        Object.prototype.toString.call(t) === "[object " + e + "]"
    }
    function n(t) {
        if (e(t, "array")) {
            for (var r = [], i = 0, o = t.length; o > i; i++)
                r.push(n(t[i]));
            return r
        }
        if (e(t, "object")) {
            var r = {};
            for (key in t)
                r[key] = n(t[key]);
            return r
        }
        return t
    }
    function r(t) {
        return t && a[t] && n(a[t])
    }
    function i(t, e) {
        return t && (a[t] = e),
        e
    }
    function o(t) {
        return e(t, "object") && (a = t),
        n(a)
    }
    t.__M = t.__M || {};
    var a = {};
    t.__M.get = r,
    t.__M.set = i,
    t.__M.context = o
}(this)