VHOST=www.primianotucci.com
OUT=htdocs
SCSS=pyscss --images-root=images --images-url=/static/images --no-debug-info -C
OPTIPNG=optipng -o2 -quiet
SHASUM=python -c "import hashlib,sys; h=hashlib.sha1(); h.update(open(sys.argv[1]).read()); print h.hexdigest()[0:8]"
RENDER=python render.py --out-base-dir $(OUT)

ASSETS_IMAGES=$(wildcard assets/images/*.png)
ASSETS_IMAGES+=$(wildcard assets/images/*.jpg)
ASSETS_IMAGES+=$(wildcard assets/images/*.ico)
PARTIAL_TEMPLATES=$(wildcard templates/_*.html)

all: home

$(OUT)/.mkdir $(OUT)/%/.mkdir:
	@mkdir -p $(dir $(abspath $@))
	@touch $(abspath $@)

$(OUT)/index.html: templates/home.html \
                   $(PARTIAL_TEMPLATES) \
                   $(OUT)/static/.stamp \
                   render.py \
                   | $(OUT)/.mkdir
	$(RENDER) --template-in $< \
            --var vhost=$(VHOST) \
            --html-out $@

$(OUT)/static/css/%.css.in: assets/css/%.scss \
                            $(wildcard assets/css/_*.scss) \
                            $(wildcard assets/images/*) \
                            | $(OUT)/static/css/.mkdir
	$(SCSS) $< -o $@

$(OUT)/static/images/%.png.in: assets/images/%.png \
                               | $(OUT)/static/images/.mkdir
	@cp -f $< $@
	$(OPTIPNG) $@

$(OUT)/static/images/%.in: assets/images/% \
                           | $(OUT)/static/images/.mkdir
	@cp -f $< $@

$(OUT)/static/js/%.in: assets/js/% \
                       | $(OUT)/static/js/.mkdir
	@cp -f $< $@

$(OUT)/static/fonts/.stamp: assets/fonts/* | $(OUT)/static/fonts/.mkdir
	cp -rf assets/fonts/* $(OUT)/static/fonts/
	touch $@

$(OUT)/static/.stamp: \
    $(patsubst assets/images/%,$(OUT)/static/images/%,$(ASSETS_IMAGES)) \
		$(patsubst assets/css/%.scss,$(OUT)/static/css/%.css,$(wildcard assets/css/[a-z]*.scss)) \
    $(patsubst assets/js/%,$(OUT)/static/js/%,$(wildcard assets/js/*.js)) \
    $(OUT)/static/fonts/.stamp \
    | $(OUT)/static/images/.mkdir \
      $(OUT)/static/fonts/.mkdir \
      $(OUT)/static/css/.mkdir \
      $(OUT)/static/js/.mkdir
	touch $@

$(OUT)/static/% : $(OUT)/static/%.in
	$(eval SHA := $(shell $(SHASUM) $<))
	$(eval TARGET := $(basename $@)-$(SHA)$(suffix $@))
	@cp $< $(basename $@)-$(SHA)$(suffix $@)
	@ln -fs $(notdir $(TARGET)) $@

$(OUT)/%: assets/%
	cp $(patsubst $(OUT)/%,assets/%,$@) $@

home: $(OUT)/index.html $(OUT)/robots.txt $(OUT)/robots-allow.txt $(OUT)/googlee356e6e521375c87.html
images: $(OUT)/static/images/.stamp

dev:
	dev_appserver.py .

deploy:
	gcloud app deploy --project primianotucci-com
	@echo 'Done. Remember to push to github'

clean:
	rm -rf $(OUT)/*

.PHONY: all home images dev clean
