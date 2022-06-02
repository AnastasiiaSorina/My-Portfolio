function AnsiSlider () {
    this.imgsUrls = [];
    this.currentImageIndex = 0;

    this.showPrevBtn = null;
    this.showNextBtn = null;
    this.slideImg = null;
    this.start = function (elId) {
        var that = this;

        var elSelector = '#' + elId;
        var el = document.querySelector(elSelector);

        this.showPrevBtn = el.querySelector('.show-prev-btn');
        this.showNextBtn = el.querySelector('.show-next-btn');
        this.slideImg = el.querySelector('.slide-img');

        //subscribe to events
        this.showPrevBtn.addEventListener('click', function (e) {
            that.onShowPrevBtnClic(e);
        });
        this.showNextBtn.addEventListener('click', function (e) {
            that.onShowNextBtnClic(e);
        });

        // create images arry
        this.imgsUrls.push('https://fingazeta.ru/sites/default/files/2020-09/maxresdefault_0.jpg');
        this.imgsUrls.push('https://repost.uz/storage/uploads/0-1628059518-nadira-post-material.jpeg');
        this.imgsUrls.push('https://glavcom.ua/img/article/5645/90_main.jpg');
        this.imgsUrls.push('https://automotyw.com/wp-content/uploads/2021/01/2021-tesla-model-s-update-blue-1611800348.jpg');

        this.slideImg.src = this.imgsUrls[this.currentImageIndex];
        this.showPrevBtn.disabled = true;
    };
    this.onShowPrevBtnClic = function (e) {
        this.currentImageIndex--;
        this.slideImg.src = this.imgsUrls[this.currentImageIndex];
        this.showNextBtn.disabled = false;

        //disable prev button if need
        if (this.currentImageIndex === 0) {
            this.showPrevBtn.disabled = true;
        }
    };
    this.onShowNextBtnClic = function (e) {
        this.currentImageIndex++;
        this.slideImg.src = this.imgsUrls[this.currentImageIndex];
        this.showPrevBtn.disabled = false;

        //disable next button if need
        if (this.currentImageIndex === (this.imgsUrls.length - 1)) {
            this.showNextBtn.disabled = true;
        }
    };
}