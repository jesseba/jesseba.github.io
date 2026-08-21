# Generates one page per photography chapter.
#
# A collection page lists its chapters as cover tiles; each chapter gets its own
# page at /photography/<collection>/<chapter>/. Doing this in a generator rather
# than by hand means adding a chapter to _data/photography.yml is enough — no
# page file to create, and chapters with no photographs never get a page at all.
#
# Chapter urls come from the chapter's `tag`, not its name, so rewording a
# heading does not change the url. That mirrors how the importers match photos.

module Jekyll
  class PhotographyChapterPage < PageWithoutAFile
    def initialize(site, collection, chapter, siblings, index)
      super(site, site.source, File.join("photography", collection["slug"], chapter["url"]), "index.html")

      previous_chapter = index > 0 ? siblings[index - 1] : nil
      next_chapter = index < siblings.length - 1 ? siblings[index + 1] : nil

      data.merge!(
        "layout" => "chapter",
        "title" => chapter["name"],
        "description" => "#{chapter['name']} — #{collection['title']}, #{collection['year']}",
        "nav" => false,
        "gallery" => collection["slug"],
        "chapter" => chapter["name"],
        "chapter_position" => index + 1,
        "chapter_total" => siblings.length,
        "prev_chapter" => previous_chapter,
        "next_chapter" => next_chapter
      )
    end
  end

  class PhotographyChapters < Jekyll::Generator
    safe true
    priority :normal

    def generate(site)
      collections = site.data["photography"]
      return if collections.nil?

      collections.each do |collection|
        next unless collection["group_by_location"]

        manifest = (site.data.dig("photos", collection["slug"]) || [])
        next if manifest.empty?

        counts = manifest.group_by { |photo| photo["location"] }.transform_values(&:size)

        # Only chapters that actually have photographs, in config order.
        chapters = (collection["locations"] || []).filter_map do |entry|
          name = entry.is_a?(Hash) ? entry["name"] : entry
          tag = entry.is_a?(Hash) ? (entry["tag"] || name) : name
          count = counts[name].to_i
          next if count.zero?

          cover = manifest.find { |photo| photo["location"] == name }
          {
            "name" => name,
            "url" => slugify(tag),
            "count" => count,
            "cover" => cover
          }
        end
        next if chapters.empty?

        chapters.each_with_index do |chapter, index|
          site.pages << PhotographyChapterPage.new(site, collection, chapter, chapters, index)
        end

        # Handed to the collection page so it can render tiles without
        # recomputing any of this in Liquid.
        collection["chapters"] = chapters
      end
    end

    private

    def slugify(value)
      value.to_s.downcase.gsub(/[^a-z0-9]+/, "-").gsub(/\A-|-\z/, "")
    end
  end
end
