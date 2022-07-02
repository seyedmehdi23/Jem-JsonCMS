function textarea_modify_size() {
    var elemes = document.body.getElementsByTagName("textarea");
    for (let i = 0; i < elemes.length; i++) {
        elemes[i].addEventListener('input', function () {
            this.style.overflow = 'hidden';
            this.style.height = 0;
            this.style.height = this.scrollHeight + 'px';
        }, false);
    }
}

textarea_modify_size();