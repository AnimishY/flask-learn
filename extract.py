import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install the beautifulsoup4 package.")
    sys.exit(1)

html_code = '''
<article
    data-v-c6a23bca=""
    data-v-3cea1acf=""
    class="speaker-card"
  >
    <figure data-v-c6a23bca="" class="opensSpeakerInfo">
      <img
        data-v-c6a23bca=""
        class="speaker_"
        src="./Speakers_files/310-240.png"
        loading="lazy"
        alt="Hon&#39;ble PM Shri Narendra Modi"
      />
      <figcaption data-v-c6a23bca="">
        <h5
          data-v-c6a23bca=""
          title="Hon&#39;ble PM Shri Narendra Modi"
        >
          Hon'ble PM Shri Narendra Modi
        </h5>
        <ul data-v-c6a23bca="">
          <li
            data-v-c6a23bca=""
            title="Prime Minister of India"
            class="post"
          >
            <img
              data-v-c6a23bca=""
              src="./Speakers_files/user-small.svg"
            />
            Prime Minister of India
          </li>
          <li
            data-v-c6a23bca=""
            title="Govt. of India"
            class="niche"
          >
            <img
              data-v-c6a23bca=""
              src="./Speakers_files/office-small.svg"
            />
            Govt. of India
          </li>
        </ul>
        <button data-v-c6a23bca="">
          <svg
            data-v-c6a23bca=""
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              data-v-c6a23bca=""
              d="M10.5 7.5L15 12L10.5 16.5"
              stroke="#1A1A1A"
              stroke-width="0.9"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></path>
          </svg>
        </button>
      </figcaption>
    </figure>
    <dialog data-v-01467258="" data-v-c6a23bca="" id="peopleModal">
      <!----><button data-v-01467258="" id="closesModal">
        <svg
          data-v-01467258=""
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            data-v-01467258=""
            d="M13.4099 11.9999L17.7099 7.70994C17.8982 7.52164 18.004 7.26624 18.004 6.99994C18.004 6.73364 17.8982 6.47825 17.7099 6.28994C17.5216 6.10164 17.2662 5.99585 16.9999 5.99585C16.7336 5.99585 16.4782 6.10164 16.2899 6.28994L11.9999 10.5899L7.70994 6.28994C7.52164 6.10164 7.26624 5.99585 6.99994 5.99585C6.73364 5.99585 6.47824 6.10164 6.28994 6.28994C6.10164 6.47825 5.99585 6.73364 5.99585 6.99994C5.99585 7.26624 6.10164 7.52164 6.28994 7.70994L10.5899 11.9999L6.28994 16.2899C6.19621 16.3829 6.12182 16.4935 6.07105 16.6154C6.02028 16.7372 5.99414 16.8679 5.99414 16.9999C5.99414 17.132 6.02028 17.2627 6.07105 17.3845C6.12182 17.5064 6.19621 17.617 6.28994 17.7099C6.3829 17.8037 6.4935 17.8781 6.61536 17.9288C6.73722 17.9796 6.86793 18.0057 6.99994 18.0057C7.13195 18.0057 7.26266 17.9796 7.38452 17.9288C7.50638 17.8781 7.61698 17.8037 7.70994 17.7099L11.9999 13.4099L16.2899 17.7099C16.3829 17.8037 16.4935 17.8781 16.6154 17.9288C16.7372 17.9796 16.8679 18.0057 16.9999 18.0057C17.132 18.0057 17.2627 17.9796 17.3845 17.9288C17.5064 17.8781 17.617 17.8037 17.7099 17.7099C17.8037 17.617 17.8781 17.5064 17.9288 17.3845C17.9796 17.2627 18.0057 17.132 18.0057 16.9999C18.0057 16.8679 17.9796 16.7372 17.9288 16.6154C17.8781 16.4935 17.8037 16.3829 17.7099 16.2899L13.4099 11.9999Z"
            fill="#A0A0A0"
          ></path>
        </svg>
      </button>
    </dialog>
  </article>
'''

soup = BeautifulSoup(html_code, 'html.parser')

speaker_name = soup.find('h5').text.strip()
job = soup.find('li', class_='post').text.strip()
description = soup.find('li', class_='niche').text.strip()

print("Speaker Name:", speaker_name)
print("Job:", job)
print("Description:", description)
